FROM python:3.8.13-alpine3.16

WORKDIR /flask_market_app

ENV FLASK_APP run.py
ENV FLASK_DEBUG 1
ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]