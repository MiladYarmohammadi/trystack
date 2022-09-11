FROM python:3.10

COPY requirements.txt /
RUN pip install -U pip setuptools
RUN pip install -r /requirements.txt

COPY . /
WORKDIR /
ENV TRYSTACK_API_DATABASE_URI=mysql+pymysql://root:yjMtjiBepvKI6cHqTHPc0BFvMaTK0hh6@trystkdb.miladsphinx.svc:3306/trystack
RUN flask --app trystack db upgrade
ENTRYPOINT ["flask"]
CMD ["run"]
