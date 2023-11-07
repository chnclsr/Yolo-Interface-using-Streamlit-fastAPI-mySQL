from fastapi import FastAPI
import base64
from PIL import Image
import io
import uvicorn
from detector import Detector
from dataclass import *

yoloAPI = FastAPI()
detector = Detector()

@yoloAPI.get("/")
async def start():
    return "YOLO_v5 based API started".encode()

@yoloAPI.post("/test")
async def test_method(data: ImageDataClass):
    img = Image.open(io.BytesIO(base64.b64decode(data.imageBase64)))
    out = detector.infer_image(img)
    return out

@yoloAPI.post("/device")
async def set_device(d: DeviceDataClass):
    if not d.device == detector.device:
        detector.device = d.device
        detector.model2device()
    response = {"device": detector.device}
    return response

def start():
    uvicorn.run(yoloAPI, host='0.0.0.0', port=8000)

if __name__ == "__main__":
    start()















