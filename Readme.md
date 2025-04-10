# Reto CTF: Vulnerabilidad XSS sencilla 

Este proyecto crea un entorno Docker para practicar técnicas de ciberseguridad, enfocado en la explotación de vulnerabilidades web.

## Configuración

El entorno contiene:
- Un servidor web Flask con python
- Una página web vulnerable que permite ver la flag 

## Puesta en marcha

1. Asegúrate de tener Docker y Docker Compose instalados en tu sistema.

2. Clona este repositorio o copia los archivos `Dockerfile` y `docker-compose.yml` a un directorio.

3. Desde el directorio que contiene los archivos, ejecuta:

```bash
docker-compose up -d
# xss-challenge
