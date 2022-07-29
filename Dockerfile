FROM python:3.7-slim-stretch

RUN pip install yamale

COPY . /

RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "sh", "-c", "/entrypoint.sh $INPUT_VALIDATORS_REQUIREMENTS" ]