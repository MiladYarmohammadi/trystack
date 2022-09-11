FROM python:3.10.7-alpine

COPY requirements.txt /
RUN python -m pip install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["gunicorn"]
CMD ["trystack:create_app"]
