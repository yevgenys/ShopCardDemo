FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

RUN mkdir ./static

EXPOSE 8000

RUN chmod +x ./dev-entrypoint.sh