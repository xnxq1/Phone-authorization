FROM python:3.11-alpine3.15
WORKDIR /app
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt