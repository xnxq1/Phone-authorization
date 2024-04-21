FROM python:3.11-alpine3.15
WORKDIR /app
COPY requirements.txt /requirements.txt
COPY app /app
EXPOSE 8000
RUN pip install -r /requirements.txt
