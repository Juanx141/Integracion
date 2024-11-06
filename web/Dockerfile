# Usar la imagen oficial de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos locales al contenedor
COPY . /app

# Instalar el conector de MySQL para Python
RUN pip install mysql-connector-python

# Comando para ejecutar el script de Python
CMD ["python", "conexion.py"]
