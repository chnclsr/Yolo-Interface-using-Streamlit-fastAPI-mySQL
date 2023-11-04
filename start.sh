#!/bin/bash -l
eval "$(conda shell.bash hook)"
conda activate streamlit-demo
python ./API/yolo_fastapi.py & sleep 3 & streamlit run main.py
echo "FastAPI for YOLO started"

