FROM python:slim

LABEL maintainer="Milad Yarmohammadi <milad.yarmohammadi94@gmail.com>"

ENV TRYSTACK_API_ENV=PRODUCTION TRYSTACK_API_DEBUG=0 TRYSTACK_API_DATABASE_URI=None TRYSTACK_API_DEFAULT_PROJECT_STATUS=0

EXPOSE 8000/tcp

WORKDIR /opt/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ./start
