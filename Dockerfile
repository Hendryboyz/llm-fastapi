FROM python:3.13.11-alpine3.23


WORKDIR /app


COPY ./requirements.txt /app/requirements.txt
COPY ./configs/local.env /app/.env


RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./src /app/src


CMD ["fastapi", "run", "src/main.py", "--port", "80"]