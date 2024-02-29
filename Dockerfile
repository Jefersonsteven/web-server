# El archivo Dockerfile es un archivo de texto que contiene los comandos que un usuario podría llamar en la línea de comandos para ensamblar una imagen.

# FROM es la imagen base que se usará para construir la imagen
FROM python:3.10

# WORKDIR establece el directorio de trabajo para cualquier comando RUN, CMD, ENTRYPOINT, COPY y ADD que siga en el Dockerfile
WORKDIR /app-web-service

# COPY copia requirements.txt a /app en el contenedor
COPY requirements.txt /app-web-service/requirements.txt

# RUN ejecuta cualquier comando en una nueva capa sobre la imagen y guarda el resultado
# Con este comando se instalan las dependencias del proyecto
RUN pip install --no-cache-dir --upgrade -r /app-web-service/requirements.txt

# COPY copia los archivos de la carpeta actual a la carpeta /app en el contenedor
COPY . /app-web-service

# CMD proporciona valores predeterminados para un contenedor en ejecución
# En este caso, se ejecuta el comando para iniciar el servidor de la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]