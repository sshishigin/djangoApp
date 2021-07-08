FROM python:3.9-buster as base

# set environment variables
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /code
WORKDIR /code

# GDAL and PROJ installation
RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy files
COPY ./entrypoint.sh /code/entrypoint.sh
COPY . /code

ENTRYPOINT ["/code/entrypoint.sh"]

EXPOSE 8000


