from dotenv import load_dotenv
import os

path = ".env"
load_dotenv(dotenv_path = path)  

#MongoDB
mongodb_host_test = os.getenv("MONGODB_HOST_TEST")
mongodb_port_test = os.getenv("MONGODB_PORT_TEST")
mongodb_database_name_test = os.getenv("MONGODB_DATABASE_NAME_TEST")
mongodb_connection_url_test = f"mongodb://{mongodb_host_test}:{mongodb_port_test}"

#Google
gemini_flash_test = os.getenv("GEMINI_API_Key_TEST")
gemini_model_name_flash_test = os.getenv("GEMINI_MODEL_NAME_FLASH_TEST")
