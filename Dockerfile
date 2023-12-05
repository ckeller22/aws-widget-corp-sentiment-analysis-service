# syntax=docker/dockerfile:1
FROM python:3.11

WORKDIR /code

ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]