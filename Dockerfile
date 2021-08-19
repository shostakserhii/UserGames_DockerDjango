FROM python:3.8

# RUN apt-get update && apt-get install -y mariadb-client && rm -rf /var/lib/apt
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install -r requirements.txt

RUN chmod 777 ./run.sh
# ENTRYPOINT ["/bin/sh"]

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# ALTER USER 'root' IDENTIFIED WITH mysql_native_password BY '123';