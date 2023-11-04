import cv2
import time
import base64
import json
from logallcommand import LoggingData


class App:
    def __init__(self, st_, worker, data_loader, logger):
        self.st = st_
        self.worker = worker
        self.divider = 10
        self.data_loader = data_loader
        self.logger = logger
        self.device = "cpu"
        self.http_client = None

    def set_http_client(self, http_client):
        self.http_client = http_client

    def add_state2db(self):
        self.worker.request_counter += 1
        remain = self.worker.request_counter % self.divider
        if remain == 0:
            val = ("request {}".format(self.worker.request_counter // self.divider), str(time.time()))
            self.worker.add_values2chosen_db(val)

    def process_video(self):
        fps = 0
        custom_size = self.st.sidebar.checkbox("Custom frame size", value=True)
        if custom_size:
            self.logger.execute(LoggingData(device="cpu", fps=fps))

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
            fps = round(1 / (curr_time - prev_time))
            prev_time = curr_time
            self.logger.LogF.st_text.markdown(f"**{fps}**")
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
        if self.http_client is None:
            raise Exception("Http client is not set. Use set_http_client method to set it.")
        encoded_string = base64.b64encode(cv2.imencode('.png', frame)[1])
        data = {'imageBase64': encoded_string.decode('UTF-8')}
        response = self.http_client.post_request("test", data)
        if response.status_code == 200:
            detections = json.loads(response.json())
            self.add_state2db()
            return detections
        else:
            print(f"Error: HTTP request was not successful ({response.status_code})")
            return None

    def changeDevice(self, device):
        if self.http_client is None:
            raise Exception("Http client is not set. Use set_http_client method to set it.")
        data = {"device": device}
        response = self.http_client.post_request("device", data)
        if response.status_code == 200:
            self.device = response.json()["device"]
        else:
            print(f"Error: HTTP request was not successful ({response.status_code})")






