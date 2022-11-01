FROM python:3.11.0-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./version1/stream_reporter.py" ]

ENV PYTHONUNBUFFERED=1