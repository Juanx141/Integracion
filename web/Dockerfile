FROM python:3.8-slim


WORKDIR /app


RUN echo 'APT::Update::Post-Invoke-Success "exit 0;";' > /etc/apt/apt.conf.d/99disable-post-invoke && \
    echo 'DPkg::Post-Invoke {"exit 0;";};' >> /etc/apt/apt.conf.d/99disable-post-invoke


RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


COPY requirements.txt ./


RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt


COPY . .


CMD ["python", "conexion.py"]