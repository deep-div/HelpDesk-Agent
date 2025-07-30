FROM python:3.11.3-slim

# Set custom working directory in container- Will be present inside container 
WORKDIR /HelpDesk-Agent

# Copy necessary files and folders into container
COPY backend /HelpDesk-Agent/backend
COPY frontend /HelpDesk-Agent/frontend
COPY requirements.txt /HelpDesk-Agent

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r /HelpDesk-Agent/requirements.txt

# Set PYTHONPATH for proper imports
ENV PYTHONPATH=/HelpDesk-Agent

# Expose FastAPI and Streamlit ports
EXPOSE 8000 7000

# Run both backend and frontend via the script
CMD ["bash", "start.sh"]
