#!/usr/bin/python

from time import sleep
from pymysql import connect
from os import environ
from sys import exit

ok = False

for i in range(1, 11):
    try:
        connection = connect(host=environ.get("TRYSTACK_API_DATABASE_HOST", "MYSQL"),
                             port=int(environ.get("TRYSTACK_API_DATABASE_PORT", "3306")),
                             user=environ.get("TRYSTACK_API_DATABASE_USER", "trystack"),
                             password=environ.get("TRYSTACK_API_DATABASE_PASSWORD", "trystack"),
                             database=environ.get("TRYSTACK_API_DATABASE_DATABASE", "trystack"))
    except:
        print(f"#{i} triage to connect to db failed!")
        sleep(10)
    else:
        with connection.cursor() as cursor:
            if cursor.execute("SELECT database();") != 1:
                print(f"#{i} triage to execute SQL failed!")
            else:
                ok = True
                
if ok:
    print("All Good!!!")
    exit(0)
else:
    print("Cannot Connect to MySQL Server")
    exit(1)
