import cv2

class DataLoader:
    def __init__(self, vid_file = "data/sample_videos/video.mp4"):
        self.VC = None
        self.vid_file = vid_file
        self.width  = None
        self.height = None

    def getVideoLoader(self):
        self.VC = cv2.VideoCapture(self.vid_file)
        self.width = int(self.VC.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.VC.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_frame_from_vc(self):
        ret, frame = self.VC.read()
        frame = cv2.resize(frame, (self.width, self.height))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return ret, frame