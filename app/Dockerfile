FROM python:3.8-alpine

RUN apk update && \
    apk add --no-cache postgresql-dev gcc python3-dev musl-dev build-base

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]