FROM python:3.9.7

ADD ./Docker/Python-runner/requirements.txt requirements.txt

RUN pip --no-cache-dir install --upgrade -r requirements.txt

ADD ./ /home

WORKDIR /home