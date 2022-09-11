FROM python:3.10.7-alpine

COPY requirements.txt /
RUN python -m pip install -r /requirements.txt

COPY . /
WORKDIR /

ENTRYPOINT ["gunicorn"]
CMD ["trystack:create_app"]
