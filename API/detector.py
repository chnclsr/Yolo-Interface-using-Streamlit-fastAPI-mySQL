import torch
import json


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
                                    path="../models/yolov5s.pt",
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
