FROM python:3.7.4-alpine3.10

COPY bot ./bot
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["python", "-m", "bot"]