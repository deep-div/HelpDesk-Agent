FROM python:3.11.3-slim

# Set custom working directory in container
WORKDIR /HelpDesk-Agent-frontend

# Copy necessary files and folders into container
COPY frontend /HelpDesk-Agent-frontend/frontend
COPY requirements.txt /HelpDesk-Agent-frontend

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r /HelpDesk-Agent-frontend/requirements.txt

# Set PYTHONPATH for proper imports
ENV PYTHONPATH=/HelpDesk-Agent-frontend

# Expose FastAPI port
EXPOSE 7000 

# Run FastAPI app with uvicorn
CMD ["streamlit", "run", "frontend/streamlit_ui.py", "--server.port=7000", "--server.address=0.0.0.0"]
