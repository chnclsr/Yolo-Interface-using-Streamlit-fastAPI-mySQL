from fastapi import FastAPI, File, Request, UploadFile
from pydantic import BaseModel
import base64
import numpy as np
from PIL import Image
import io
import uvicorn
import torch
import json


class ImageClass(BaseModel):
    imageBase64: str

class DeviceClass(BaseModel):
    device: str

class Detector:
    def __init__(self):
        self.model = None
        self.device = "cpu"
        self.load_model()

    def model2device(self):
        self.model.to(self.device)

    def load_model(self):
        torch.hub._validate_not_a_forked_repo = lambda a, b, c: True
        self.model = torch.hub.load('ultralytics/yolov5',
                                'custom',
                                path="./models/yolov5s.pt",
                                force_reload=True)
        self.model2device()

    def infer_image(self, img, size=None):
        results = self.model(img, size=size) if size else self.model(img)
        detections = []
        for pred in results.pred:
            for det in pred:
                # Bbox koordinatlarını alın
                bbox = det[:4].tolist()
                # Sınıf etiketini ve güveni alın
                class_id = int(det[5])
                confidence = float(det[4])
                # Sonuçları listeye ekleyin
                detections.append({
                    "class_id": class_id,
                    "confidence": confidence,
                    "bbox": bbox
                })
        json_result = json.dumps(detections, indent=4)
        return json_result



yoloAPI = FastAPI()
detector = Detector()

@yoloAPI.post("/test")
async def test_method(data: ImageClass):
    img = Image.open(io.BytesIO(base64.b64decode(data.imageBase64)))
    out = detector.infer_image(img)
    return out


@yoloAPI.get("/")
async def start():
    return "started".encode()

@yoloAPI.post("/device")
async def set_device(d: DeviceClass):
    if not d.device == detector.device:
        detector.device = d.device
        detector.model2device()

    response = {"device": detector.device}
    return response

def start():
    uvicorn.run(yoloAPI, host='0.0.0.0', port=8000)

if __name__ == "__main__":
    start()















