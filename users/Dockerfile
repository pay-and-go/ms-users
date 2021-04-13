FROM python:3.7.4

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
#RUN apt-get install -y python3-pymysql
RUN apt update -y && apt upgrade -y && apt-get install -y build-essential
#RUN apt-get install python-dev
RUN apt-get install -y python-dev && apt-get install -y python3-pymysql
RUN pip install pymysql
RUN pip install -r requirements.txt
#RUN apt install libmysqlclient-dev
COPY . /code/
ARG URL=0.0.0.0:4000

CMD ["sh", "-c", "python manage.py makemigrations users && python manage.py migrate && python manage.py runserver $URL"]