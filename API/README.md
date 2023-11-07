# YOLO_v5 Object Detection API (using fastAPI)
This is a FastAPI-based API that utilizes the YOLOv5 model for object detection. YOLOv5 is a state-of-the-art real-time object detection model that can be used to identify and locate objects in images.

## Installation
Clone this repository to your local machine:
```python
git clone https://github.com/autoM-coder/Yolo-Interface-using-Streamlit-fastAPI-mySQL.git
```

Install the required Python packages using pip:
```python
pip install -r requirements.txt
```


### Usage
Start the API by running the start() function in the main.py file:

```python
python yolo_fastapi.py
```

The API will start and be accessible
at http://localhost:8000 by default.

### Endpoints
The API provides the following endpoints:

GET /

- Description: Check if the API is running.
- Response: "YOLO_v5 based API started".

POST /test

- Description: Perform object detection on an image.
- Request Data: imageBase64 (base64-encoded image).
- Response: JSON containing object detection results, 
including class IDs, confidence scores, and bounding box
coordinates.

POST /device

- Description: Set the device (CPU or CUDA) for inference.
- Request Data: device (e.g., "cpu" or "cuda").
- Response: JSON confirming the selected device.

## Author
[chncalisir]

