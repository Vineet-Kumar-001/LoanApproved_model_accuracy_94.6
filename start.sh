#!/bin/bash

uvicorn app.api:app --host 0.0.0.0 --port 8000 &

sleep 5

streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0