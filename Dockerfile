FROM python:3.7

RUN apt-get update \
    && apt-get -y install vim bash-completion
RUN echo ". /etc/bash_completion" >> /root/.bashrc
RUN pip install pipenv

WORKDIR /project-home

CMD tail -f /dev/null
