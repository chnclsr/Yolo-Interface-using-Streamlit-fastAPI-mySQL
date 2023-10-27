FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11
USER root
RUN apt update
RUN #apt-get install sudo
RUN apt-get update && apt-get install libgl1 -y

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
RUN chmod 777 start_in_docker.sh
# https://linuxconfig.org/how-to-install-kubernetes-on-ubuntu-22-04-jammy-jellyfish-linux
#EXPOSE 8000
EXPOSE 80

# install minikube
# https://linux.how2shout.com/how-to-install-minikube-on-ubuntu-22-04-lts-linux/
# CMD ["source", "./start_in_docker.sh"]