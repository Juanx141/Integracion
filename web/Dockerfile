FROM python:3.8-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Deshabilitar los scripts post-invocación de APT
RUN echo 'APT::Update::Post-Invoke-Success {"none";};' > /etc/apt/apt.conf.d/99disable-post-invoke

# Actualizar APT e instalar dependencias necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de dependencias
COPY requirements.txt ./

# Instalar las dependencias de Python
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar el contenido restante del proyecto
COPY . /app/

# Comando por defecto para ejecutar la aplicación
CMD ["python", "conexion.py"]