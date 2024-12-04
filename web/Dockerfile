FROM python:3.8-slim


WORKDIR /app


ENV DEBIAN_FRONTEND=noninteractive


RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean


COPY requirements.txt .


RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["python", "conexion.py"]
