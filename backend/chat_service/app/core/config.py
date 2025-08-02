from dotenv import load_dotenv
import os

path = ".env"
load_dotenv(dotenv_path = path)  

#Google
gemini_flash_test = os.getenv("GEMINI_API_Key_TEST")
gemini_model_name_flash_test = os.getenv("GEMINI_MODEL_NAME_FLASH_TEST")

# Url
url_chat_service = os.getenv("CHAT_SERVICE")
url_mongodb_service = os.getenv("MONGODB_SERVICE")