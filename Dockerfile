FROM python:3.11

RUN useradd -m app

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

USER app

ENV PYTHONPATH=/app

ENTRYPOINT ["python3", "-u", "/app/src/main.py"]