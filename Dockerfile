FROM python:3.7
MAINTAINER Charles Tapley Hoyt "cthoyt@gmail.com"

RUN pip install --upgrade pip
RUN pip install pipenv

ADD requirements.txt zoo/requirements.txt
RUN pip install zoo/requirements.txt

ADD zoo.py /zoo/zoo.py
WORKDIR /zoo
