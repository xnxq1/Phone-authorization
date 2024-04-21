FROM python:3.11-alpine3.15
WORKDIR /app
COPY requirements.txt /requirements.txt
COPY app /app
EXPOSE 8000
RUN apk add gcc musl-dev
RUN apk add postgresql-dev
RUN pip install -r /requirements.txt
