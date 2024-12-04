FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias necesarias para compilar extensiones de Python
RUN apt-get update && apt-get install -y \
    gcc libffi-dev libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar el archivo de requisitos
COPY requirements.txt .

# Actualizar pip e instalar dependencias desde requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Comando por defecto para ejecutar el programa
CMD ["python", "conexion.py"]
