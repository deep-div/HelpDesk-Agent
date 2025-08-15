# HelpDesk-AI
 
      

https://github.com/user-attachments/assets/b5d9a3e8-9d80-444e-9123-2bdca5c49562



A simple and efficient AI-powered Helpdesk system where users can register complaints, track their status, and get automated assistance. This project integrates Google's **Gemini Flash** model to assist in handling user queries and issues.
 
---

## 📁 Project Structure

```
HelpDesk-Agent/
│
├── .venv/                                 # Virtual environment (Python)
├── .env                                   # Environment variables (secrets, configs)
├── .gitignore                             # Git ignore rules
├── LICENSE                                # License file
├── pyproject.toml                         # Project dependencies & metadata
├── docker-compose-chat-service.yml       # Docker Compose for chat microservice
├── docker-compose-frontend.yml           # Docker Compose for frontend service
├── docker-compose-mongodb-service.yml    # Docker Compose for MongoDB microservice
│
├── backend/
│   ├── chat_service/
│   │   ├── app/
│   │   │   ├── apis/
│   │   │   │   ├── apis_clients.py
│   │   │   │   └── chat_routes.py
│   │   │   ├── core/
│   │   │   │   ├── clients.py
│   │   │   │   └── config.py
│   │   │   ├── gemini/
│   │   │   │   ├── gemini_history.py
│   │   │   │   ├── gemini_llm.py
│   │   │   │   ├── gemini_tools.py
│   │   │   │   └── system_prompt.py
│   │   │   ├── models/
│   │   │   │   └── data_models.py
│   │   ├── main.py                        # Entry point for chat service
│   │   └── Dockerfile
│
│   ├── mongodb_service/
│   │   ├── app/
│   │   │   ├── apis/
│   │   │   │   ├── apis_clients.py
│   │   │   │   └── mongodb_routes.py
│   │   │   ├── core/
│   │   │   │   ├── clients.py
│   │   │   │   └── config.py
│   │   │   ├── models/
│   │   │   │   ├── data_models.py
│   │   │   │   └── db_schemas.py
│   │   │   ├── mongodb/
│   │   │   │   ├── __init__.py
│   │   │   │   └── db_connections.py
│   │   ├── main.py                        # Entry point for MongoDB service
│   │   └── Dockerfile
│
├── frontend/
│   ├── apis/
│   │   └── apis_clients.py
│   ├── images/
│   ├── streamlit_ui.py                   # Main Streamlit app UI
│   └── Dockerfile

```

---

## 🚀 Features

* 📝 Register user complaints
* 📊 Track and check the status of complaints
* 🤖 AI agent built with **Gemini Flash** to assist user interactions
* 🗂️ MongoDB backend for persistent storage
* ⚡ FastAPI backend
* 🎨 Streamlit frontend for simple, user-friendly UI

---



## ⚙️ Setup Instructions

> Make sure Python 3.10+ is installed and accessible via `py` or `python3`.

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd HelpDesk-AI
```

### 2. Setup Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows
.venv\Scripts\activate

# Unix/MacOS
source .venv/bin/activate
```

### 3. Install Dependencies

Make sure you have [**uv**](https://github.com/astral-sh/uv) installed.

```bash
uv sync
```

### 4. Run the Backend Services

```bash
py -m uvicorn backend.mongodb_service.main:app --reload --port 8001
```

```bash
# py -m uvicorn backend.chat_service.main:app --reload --port 8000
```

### 5. Run the Frontend UI

```bash
streamlit run .\frontend\streamlit_ui.py --server.port 7000
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following (example):

```env
## Local Configurations-------------------------------------------------------------------------------------------

# Mongo DB
MONGODB_HOST_TEST="localhost"
MONGODB_PORT_TEST="27017"
MONGODB_DATABASE_NAME_TEST="grievances"

# Gemini
GEMINI_API_Key_TEST = "key"
GEMINI_MODEL_NAME_FLASH_TEST = "gemini-2.0-flash"

# URLs
CHAT_SERVICE = "http://127.0.0.1:8000"
MONGODB_SERVICE = "http://127.0.0.1:8001"


## Docker Configurations-------------------------------------------------------------------------------------------


# # Mongo DB
# MONGODB_HOST_TEST="host.docker.internal"
# MONGODB_PORT_TEST="27017"
# MONGODB_DATABASE_NAME_TEST="grievances"

# # Gemini
# GEMINI_API_Key_TEST = "Key"
# GEMINI_MODEL_NAME_FLASH_TEST = "gemini-2.0-flash"

# # URLs
# CHAT_SERVICE = "http://chat_service:8000"
# MONGODB_SERVICE = "http://mongodb_service:8001"


```

---

## 🧠 Powered By

* [Gemini Flash (Google GenAI)](https://ai.google.dev/)
* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)
* [MongoDB](https://www.mongodb.com/)
* [uv (fast dependency manager)](https://github.com/astral-sh/uv)

---

## 📌 TODO / Future Improvements

* Add login/authentication system
* Admin dashboard for complaint management
* Notification/email integration for updates
* Improve UI/UX with chat-like interface

---

## 📃 License

This project is licensed under the MIT License - see the [LICENSE](https://chatgpt.com/c/LICENSE) file for details.

---

Let me know if you want me to auto-generate a `README.md` file in your directory structure as well.
