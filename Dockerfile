FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
