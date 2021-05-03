FROM ubuntu:18.04

WORKDIR /app

COPY requirements /tmp/requirements

RUN apt-get update
RUN apt-get install -y python3 \
    python3-dev \
    vim \
    python3-pip \
    libmysqlclient-dev \
    python3-lxml \
    libxml2-dev \
    libxslt-dev \
    binutils \
    libproj-dev


RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN pip3 install -r /tmp/requirements/base.txt

RUN ln -s /usr/bin/python3  /usr/bin/python
RUN ln -s /usr/bin/pip3  /usr/bin/pip