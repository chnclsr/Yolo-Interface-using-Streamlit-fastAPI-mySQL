import streamlit as st
import cv2
import time
import base64
import json
import requests

headers = {'Content-type': 'application/json',
               'Accept': 'application/json'}
cfg_model_path = 'models/yolov5s.pt'
model = None
confidence = .75

class App:
    def __init__(self, st_, worker):
        self.url = "http://127.0.0.1:8000"
        self.st = st_
        self.worker = worker
        self.divider = 10


    def add_state2db(self):
        self.worker.request_counter += 1
        remain = self.worker.request_counter % self.divider
        if remain == 0:
            val = ("request {}".format(self.worker.request_counter // self.divider), str(time.time()))
            self.worker.add_values2chosen_db(val)
            # self.worker.logger.show_databases()
            # self.worker.logger.show_tables()
            # self.worker.logger.show_table_values(tableName=self.worker.settings.tableName)

    def video_input(self, data_src):
        vid_file = "data/sample_videos/video.mp4"
        cap = cv2.VideoCapture(vid_file)
        custom_size = self.st.sidebar.checkbox("Custom frame size")
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if custom_size:
            width = self.st.sidebar.number_input("Width", min_value=120, step=20, value=width)
            height = self.st.sidebar.number_input("Height", min_value=120, step=20, value=height)

        fps = 0
        st1, st2, st3 = self.st.columns(3)
        with st1:
            self.st.markdown("## Height")
            st1_text = self.st.markdown(f"{height}")
        with st2:
            self.st.markdown("## Width")
            st2_text = self.st.markdown(f"{width}")
        with st3:
            self.st.markdown("## FPS")
            st3_text = self.st.markdown(f"{fps}")

        self.st.markdown("---")
        output = self.st.empty()
        prev_time = 0
        # curr_time = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                self.st.write("Can't read frame, stream ended? Exiting ....")
                break
            frame = cv2.resize(frame, (width, height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            detections = self.getPredictionResult(frame)

            frame = self.drawDetections(frame, detections)


            output.image(frame)
            curr_time = time.time()
            fps = 1 / (curr_time - prev_time)
            prev_time = curr_time
            st1_text.markdown(f"**{height}**")
            st2_text.markdown(f"**{width}**")
            st3_text.markdown(f"**{fps:.2f}**")

        cap.release()

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
        # output_img = self.infer_image(frame)
        # output.image(output_img)
        detections = json.loads(r.json())
        self.add_state2db()
        return detections

    def changeDevice(self, device):
        data = {"device": device}
        r = requests.post("{}/device".format(self.url),
                      data=json.dumps(data),
                      headers=headers)
        self.st.text("Device: {}".format(r.json()["device"]))





