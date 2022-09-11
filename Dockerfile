FROM python:3.10.7-alpine

COPY requirements.txt /
RUN python -m pip install -r /requirements.txt

COPY . /app
WORKDIR /app

ENTRYPOINT ["./gunicorn.sh"]
CMD ["--chdir", "trystack:create_app", "-w", "2", "--threads", "2", "-b", "0.0.0.0:8000"]
