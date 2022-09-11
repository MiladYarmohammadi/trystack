FROM python:3.10

COPY requirements.txt /
RUN pip install -U pip setuptools
RUN pip install -r /requirements.txt

COPY . /
WORKDIR /

RUN flask --app trystack db upgrade
ENTRYPOINT ["flask"]
CMD ["run"]
