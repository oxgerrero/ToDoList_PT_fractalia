FROM python:3.11-slim

WORKDIR /app

COPY ./app /app/app
COPY requirements.txt .
COPY start.sh .

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x start.sh

CMD ["./start.sh"]