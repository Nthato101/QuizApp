FROM python:3.8-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3","mange.py","runserver","0.0.0.0:8000"]

