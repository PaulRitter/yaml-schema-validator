FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

RUN chmod +x entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]