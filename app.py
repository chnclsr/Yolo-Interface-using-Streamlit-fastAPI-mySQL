import cv2
import time
import base64
import json
import requests
from logallcommand import LogAllCommand, LoggingData

headers = {'Content-type': 'application/json',
            'Accept': 'application/json'}

cfg_model_path = 'models/yolov5s.pt'
model = None
confidence = .75



class App:
    def __init__(self, st_, worker, data_loader):
        self.url = "http://127.0.0.1:8000"
        self.st = st_
        self.worker = worker
        self.divider = 10
        self.data_loader = data_loader
        self.logger = LogAllCommand(self.st, self.data_loader)
        self.device = "cpu"

    def add_state2db(self):
        self.worker.request_counter += 1
        remain = self.worker.request_counter % self.divider
        if remain == 0:
            val = ("request {}".format(self.worker.request_counter // self.divider), str(time.time()))
            self.worker.add_values2chosen_db(val)
            # self.worker.logger.show_databases()
            # self.worker.logger.show_tables()
            # self.worker.logger.show_table_values(tableName=self.worker.settings.tableName)

    def process_video(self):
        fps = 0
        custom_size = self.st.sidebar.checkbox("Custom frame size", value = True)
        if custom_size:
            self.logger.execute(LoggingData(device = "cpu", fps = fps))

        self.st.markdown("---")
        output = self.st.empty()
        prev_time = 0
        while True:
            ret, frame = self.data_loader.get_frame_from_vc()
            if not ret:
                self.st.write("Can't read frame, stream ended? Exiting ....")
                break

            detections = self.getPredictionResult(frame)
            frame = self.drawDetections(frame, detections)
            output.image(frame)
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time
            self.logger.LogF.st_text.markdown(f"**{fps:.2f}**")
            self.logger.LogD.st_text.markdown(f"**{self.device}**")

        self.data_loader.VC.release()

    def drawDetections(self, frame, detections):
        for detection in detections:
            bbox = detection["bbox"]
            x1, y1, x2, y2 = map(int, bbox)
            label = f"Class: {detection['class_id']}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)
        return frame

    def getPredictionResult(self, frame):
        # img_name = "./data/d.png"
        encoded_string = base64.b64encode(cv2.imencode('.png', frame)[1])
        # os.remove(img_name)
        data = {'imageBase64': encoded_string.decode('UTF-8')}
        r = requests.post("{}/test".format(self.url),
                          data=json.dumps(data),
                          headers=headers)
        detections = json.loads(r.json())
        self.add_state2db()
        return detections

    def changeDevice(self, device):
        data = {"device": device}
        r = requests.post("{}/device".format(self.url),
                      data=json.dumps(data),
                      headers=headers)
        self.device = r.json()["device"]






