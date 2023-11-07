# Object Recognition Dashboard

This is a Python application that serves as an Object Recognition Dashboard. The dashboard is designed to process video streams, recognize objects within those streams, and visualize the results. It utilizes various libraries and components to achieve these functionalities.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/autoM-coder/Yolo-Interface-using-Streamlit-fastAPI-mySQL.git
pip install -r requirements.txt
```


## Usage
To use the Object Recognition Dashboard, follow these instructions:
- Start [YOLO API](https://github.com/autoM-coder/Yolo-Interface-using-Streamlit-fastAPI-mySQL/blob/main/API/README.md)
- Start the dashboard by running the main script:

- ```bash
  streamlit run main.py 
  ```

- The dashboard will launch in your web browser and provide options to configure device settings and initiate video processing.

- You can select the processing device (CPU or CUDA) based on the availability of your hardware.

- The dashboard will start processing video streams and performing object recognition.


## Start app with bash 

```bash
chmod 777 start.sh
./start.sh
```

## Start app with Docker

```bash
docker build -t yolo-interface-using-streamlit .
docker run -it --network host --name yolo_container_id_0 yolo-interface-using-streamlit 
```