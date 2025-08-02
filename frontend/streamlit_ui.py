import streamlit as st
from google import genai
from google.genai import types
from frontend.apis.apis_clients import Api
import uuid

apis = Api()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Unique session ID for each user
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

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

    # Backend API Connectivity
    backend_payload = {
        "session_id": st.session_state.session_id,
        "user_query": prompt,
        "history": st.session_state.messages  # full history
    }

    api_agent_response = apis.chat_ui(backend_payload)

    # Check if response is a dict and has the expected key
    if isinstance(api_agent_response, dict) and "agent_response" in api_agent_response:
        response = api_agent_response["agent_response"]

        with st.chat_message("assistant", avatar="frontend/images/cy_9346214.png"):
            st.markdown(response)

        # Save assistant message
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error("Failed to get valid response from backend.")




# streamlit run .\frontend\streamlit_ui.py --server.port 7000
