FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install customtkinter

CMD ["python", "scaling.py"]
