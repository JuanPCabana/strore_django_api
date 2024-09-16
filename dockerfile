FROM python:3.9.19-bookworm

RUN apt-get update && apt-get install -y pkg-config netcat-openbsd

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

COPY wait-for-db.sh /app/
RUN chmod +x /app/wait-for-db.sh

EXPOSE 8000
