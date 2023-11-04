from pydantic import BaseModel
class DataClass(BaseModel):
    pass

class ImageDataClass(DataClass):
    imageBase64: str

class DeviceDataClass(DataClass):
    device: str