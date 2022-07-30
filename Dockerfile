FROM python:3.7-slim-stretch

COPY . /

RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]