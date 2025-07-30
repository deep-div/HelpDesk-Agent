#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# Start FastAPI backend in the background
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend
streamlit run frontend/streamlit_ui.py --server.port=7000 --server.address=0.0.0.0
