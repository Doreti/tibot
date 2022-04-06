FROM python:3.8
LABEL MAINTAINER Kyraga
WORKDIR /app
COPY ./bot/main.py . 
COPY scripts/requirements.txt /scripts/
RUN pip install -r /scripts/requirements.txt
CMD [ "python", "./main.py" ]