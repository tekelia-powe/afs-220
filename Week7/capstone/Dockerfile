FROM python:3.10-slim-buster

WORKDIR /app

RUN  pip install --upgrade pip

RUN apt-get update

RUN apt-get install git -y

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]