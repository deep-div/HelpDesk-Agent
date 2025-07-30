import streamlit as st
from google import genai
from google.genai import types
from backend.app.gemini.gemini_tools import GeminiTools
from backend.app.gemini.gemini_llm import GeminiLLM
from backend.app.apis.apis import Api
from backend.app.gemini.gemini_history import ConversationBuilder

geminillm=GeminiLLM()
geminitools = GeminiTools(geminillm)
apis_knowledge_base = Api()
conversationbuilder = ConversationBuilder()

client = geminillm.client

if "chat" not in st.session_state:
    st.session_state.chat = client.chats.create(model=geminillm.model_id, config=geminitools.config)

if "messages" not in st.session_state:
    st.session_state.messages = []

# default mssg
if not st.session_state.messages:
    with st.chat_message("assistant",  avatar="frontend/images/cy_9346214.png"):
        st.markdown("👋 **Hi, I’m your helpdesk agent. How can I assist you today?**")


# display chat messages from history at every rerun  
for message in st.session_state.messages:
    avatar_path = (
        "frontend/images/person_15454011.png" if message["role"] == "user"
        else "frontend/images/cy_9346214.png"
    )
    with st.chat_message(message["role"], avatar=avatar_path):
        st.markdown(message["content"])
        
if prompt := st.chat_input("What is up?"):
    # show user message
    with st.chat_message("user", avatar="frontend/images/person_15454011.png"):
        st.markdown(prompt)
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # stream assistant response
    full_response = ""
    with st.chat_message("assistant", avatar="frontend/images/cy_9346214.png"):
        response_stream = st.session_state.chat.send_message_stream(prompt)
        response_placeholder = st.empty()

        for chunk in response_stream:
            if chunk.text is None:  # if response is None means a tool is hit
                with st.spinner("Tool Calling..."):
                    # if tool is hit chunk.candidates[0].content.parts[0] the list will have only one index else in streaming it can have multiple indexes also
                    tool_name = chunk.candidates[0].content.parts[0].function_call.name
                    tool_args = chunk.candidates[0].content.parts[0].function_call.args
                    if tool_name == "api_register_complaints":
                        with st.spinner("Registering your complaint..."):
                            response = apis_knowledge_base.register_complaints(tool_args)
                    if tool_name == "api_complaint_status":
                        with st.spinner("Checking complaint status..."):
                            response = apis_knowledge_base.check_status(tool_args)
                    tool_response = response  # need to append full_response to session state messages 
                    
                    # Convert the json response from the api to a friendly response
                    full_response = geminillm.generate_response(
                        "Rewrite the following output into a clear, natural language response suitable for users. "
                        "If the output contains any UTC timestamps, convert them to India Standard Time (IST, UTC+5:30). "
                        "Return only the rewritten response, formatted using Markdown. "
                        "Do not include or reference the original output.\n\n"
                        "Output: " + str(tool_response)
                    )

                    # IMP..... add the response in the chathistory can see by st.session_state.chat.get_history() see complete history you will see the content is missing there and u can also more then one conttent
                    content_only_convo = conversationbuilder.build_with_content_only(full_response)
                    st.session_state.chat.get_history().extend(content_only_convo)
                    
                    # st.markdown(st.session_state.chat.get_history())  ## for reference how chat history is working
            else:
                full_response += chunk.text
                response_placeholder.markdown(full_response + "")  # stream effect

        response_placeholder.markdown(full_response)

    # save assistant message (load all the messages to show chat type view in UI )
    st.session_state.messages.append({"role": "assistant", "content": full_response})


# streamlit run .\frontend\streamlit_ui.py --server.port 7000
