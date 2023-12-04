# syntax=docker/dockerfile:1
FROM python:3.11

WORKDIR /code

ENV FLASK_APP=app/__init__.py
ENV FLASK_RUN_HOST=0.0.0.0

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]