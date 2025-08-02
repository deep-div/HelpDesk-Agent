from google.genai.types import Part, Content, UserContent

class ConversationBuilder:
    def build_with_user_content(self, user_text: str):
        response = [
            UserContent(parts=[Part(text=user_text)]), # will get a role='user' automatically 
        ]
        return response

    def build_with_content_only(self, model_text: str):
        response = [
            Content(parts=[Part(text=model_text)], role='model')
        ]
        return response

    def build_combined(self, user_text: str, model_text: str):
        response = [
            UserContent(parts=[Part(text=user_text)]),
            Content(parts=[Part(text=model_text)], role='model')
        ]
        return response

    def get_chat_history(self, history):
        chat_history = []
        # Pair user and assistant messages
        user_text = None
        for msg in history:
            if msg.role == "user":
                user_text = msg.content
            elif msg.role == "assistant" and user_text:
                model_text = msg.content
                chat_history.extend(self.build_combined(user_text, model_text))
                user_text = None  
        return chat_history