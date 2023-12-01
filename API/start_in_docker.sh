#!/bin/bash -l
#eval "$(conda shell.bash hook)"
#conda activate streamlit-demo
python yolo_fastapi.py & sleep 3
echo "FastAPI for YOLO started"

