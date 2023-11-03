from pydantic import BaseModel

class Command:
    def __init__(self, st, data_loader):
        self.st_ = st
        self.data_loader = data_loader
        self.st_text = None

    def execute(self, st, value=None):
        pass


class LogWidthCommand(Command):
    def __init__(self, st, data_loader):
        super(LogWidthCommand, self).__init__(st, data_loader)
        self.width = self.st_.sidebar.number_input("Width", min_value=120, step=20,
                                                   value=self.data_loader.width)

    def execute(self, st, value=None):
        with st:
            self.st_.markdown("## Width")
            self.st_text = self.st_.markdown(f"{self.width}")


class LogHeightCommand(Command):
    def __init__(self, st, data_loader):
        super(LogHeightCommand, self).__init__(st, data_loader)
        self.height = self.st_.sidebar.number_input("Height", min_value=120, step=20,
                                                    value=self.data_loader.height)

    def execute(self, st, value=None):
        with st:
            self.st_.markdown("## Height")
            self.st_text = self.st_.markdown(f"{self.height}")


class LogFPSCommand(Command):
    def execute(self, st, value=None):
        with st:
            self.st_.markdown("## FPS")
            self.st_text = self.st_.markdown(f"{value}")


class LogDeviceCommand(Command):
    def execute(self, st, value=None):
        with st:
            self.st_.markdown("## DEVICE")
            self.st_text = self.st_.markdown(f"{value}")



class LoggingData(BaseModel):
    device: str
    fps: float


class LogAllCommand:
    def __init__(self, st, data_loader):
        self.st1, self.st2, self.st3, self.st4 = st.columns(4)
        self.LogW = LogWidthCommand(st, data_loader)
        self.LogH = LogHeightCommand(st, data_loader)
        self.LogF = LogFPSCommand(st, data_loader)
        self.LogD = LogDeviceCommand(st, data_loader)

    def execute(self, data: LoggingData):
        self.LogW.execute(self.st1)
        self.LogH.execute(self.st2)
        self.LogF.execute(self.st3, value=data.fps)
        self.LogD.execute(self.st4, value=data.device)