FROM python:3.7.6-alpine3.11
RUN apk add --update \
  make

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY . /flask-celery
WORKDIR /flask-celery/app

EXPOSE 9797

CMD [ "python", "./main.py" ]