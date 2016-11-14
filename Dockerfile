FROM ubuntu:latest
MAINTAINER clarkzjw <clarkzjw@gmail.com>

# Install Ubuntu and base software.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y scrot git build-essential python3 python3-dev python3-pip python3-tk && \
  rm -rf /var/lib/apt/lists/*

RUN \
  pip3 install python3-xlib && \
  pip3 install pyautogui && \
  mkdir -p /code/

# RUN
ADD ./bot.py /code/bot.py

CMD /bin/bash
