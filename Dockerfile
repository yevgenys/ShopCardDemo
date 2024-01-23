FROM python:3

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt
RUN python ./manage.py migrate

RUN mkdir ./static

EXPOSE 8000

RUN chmod +x ./dev-entrypoint.sh
ENTRYPOINT ["dev-entrypoint.sh"]