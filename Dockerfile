FROM python:3.7
MAINTAINER Charles Tapley Hoyt "cthoyt@gmail.com"

RUN pip install --upgrade pip
RUN pip install pipenv

ADD Pipfile zoo/Pipfile
ADD Pipfile.lock zoo/Pipfile.lock
RUN cd /zoo && pipenv install --system --deploy --ignore-pipfile

ADD zoo.py /zoo/zoo.py
WORKDIR /zoo
