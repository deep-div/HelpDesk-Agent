from google.genai import types
from google import genai
from backend.app.gemini.gemini_llm import GeminiLLM
from backend.app.gemini.system_prompt import system_prompt

class GeminiTools():
    def __init__(self, geminillm:GeminiLLM, result= None):
        self.geminillm = geminillm
        self.result =  result
        self.api_register_complaint = {
            "name": "api_register_complaints",
            "description": (
                "This API endpoint is used to register IT Helpdesk complaints from users. It collects the user's name, mobile number, and a detailed description of the issue or grievance. These complaints may include system outages, access issues, software malfunctions, or general IT support needs."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name of the person submitting the complaint."
                    },
                    "mobile_number": {
                        "type": "string",
                        "minLength": 10,
                        "maxLength": 10,
                        "pattern": "^[0-9]{10}$",
                        "description": "User's 10-digit mobile phone number."
                    },
                    "complaints": {
                        "type": "object",
                        "properties": {
                            "complaint_details": {
                                "type": "string",
                                "description": "Detailed description of the complaint being registered."
                            }
                        },
                        "required": ["complaint_details"],
                        "description": "An object containing the complaint description."
                    }
                },
                "required": ["name", "mobile_number", "complaints"],
            }
        }
        
        self.api_complaint_status = {
            "name": "api_complaint_status",
            "description": (
                "This API is used to check the status of a previously submitted IT Helpdesk complaint. The user must provide their registered mobile number and the complaint ID to retrieve the current status of the issue."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "mobile_number": {
                        "type": "string",
                        "minLength": 10,
                        "maxLength": 10,
                        "pattern": "^[0-9]{10}$",
                        "description": "User's 10-digit mobile number associated with the complaint."
                    },
                    "complaint_id": {
                        "type": "string",
                        "description": "The unique ID assigned to the complaint when it was registered."
                    }
                },
                "required": ["mobile_number", "complaint_id"]
            }
        }

        # Set up tools and config with the function declaration
        self.tools = types.Tool(
            function_declarations=[self.api_register_complaint,  self.api_complaint_status]
        )
        self.config = types.GenerateContentConfig(
            system_instruction=system_prompt, 
            tools=[self.tools]
        )

    # one way to pick the tools
    def pick_the_tool(self, prompt_text: str):
        contents = [
            types.Content(
                role="user",
                parts=[types.Part(text=prompt_text)]
            )
        ]

        response = self.geminillm.client.models.generate_content(
            model=self.geminillm.model_id,
            config=self.config,
            contents=contents
            
        )

        self.result = response
        return self.result
    
