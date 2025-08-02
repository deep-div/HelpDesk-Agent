FROM python:3.11.3-slim

# Set working directory (inside container)
WORKDIR /HelpDesk-Agent-backend-mongodb_service

# Copy only the mongodb_service folder into the correct path
COPY backend/mongodb_service /HelpDesk-Agent/backend/mongodb_service
COPY requirements.txt /HelpDesk-Agent

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r /HelpDesk-Agent/requirements.txt

# Set PYTHONPATH so "backend" is importable
ENV PYTHONPATH=/HelpDesk-Agent

# Expose port
EXPOSE 8000

# Start the FastAPI app (relative to PYTHONPATH)
CMD ["uvicorn", "backend.mongodb_service.main:app", "--host", "0.0.0.0", "--port", "8001"]




