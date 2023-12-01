FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
USER root
RUN apt update
RUN apt-get update && apt-get install libgl1 -y

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN chmod 777 start_in_docker.sh
# https://linuxconfig.org/how-to-install-kubernetes-on-ubuntu-22-04-jammy-jellyfish-linux
#EXPOSE 8000
EXPOSE 80


#todo: add python configuration
CMD ["./start_in_docker.sh"]