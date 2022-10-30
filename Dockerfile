FROM python:3.10

RUN mkdir -p /app
COPY requirements.txt /app/requirements.txt
RUN pip install -U pip setuptools
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
WORKDIR /app
COPY . /app
ENV TRYSTACK_API_DATABASE_URI="mysql+pymysql://root:trystack@mydb-mysql-primary:3306/trystack"
CMD flask db migrate && flask db upgrade && flask run
