#!/bin/bash -l
python ./API/yolo_fastapi.py & sleep 3 & python -m streamlit run app.py
echo "FastAPI for YOLO started"

