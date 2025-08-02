from backend.chat_service.app.core.clients import gemini_client_test
from backend.chat_service.app.core.config import gemini_model_name_flash_test
from pydantic import BaseModel
from typing import Type

class GeminiLLM:
    def __init__(self):
        self.client = gemini_client_test
        self.model_id = gemini_model_name_flash_test

    def generate_response(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
        )
        return response.text

    def stream_response(self, prompt: str):
        stream = self.client.models.generate_content_stream(
            model=self.model_id,
            contents=prompt,
        )
        for chunk in stream:
            if chunk.text:
                yield chunk.text
                
    def pydantic_response(self, prompt: str, data: Type[BaseModel]):
        response = self.client.models.generate_content(
            model=self.model_id,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": data,
            },
        )
        return response.text

 