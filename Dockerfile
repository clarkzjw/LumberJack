FROM ubuntu:latest
MAINTAINER clarkzjw <clarkzjw@gmail.com>

# Install Ubuntu and base software.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y xvfb scrot git build-essential python3 python3-dev python3-pip python3-tk && \
  rm -rf /var/lib/apt/lists/*

RUN \
  DISPLAY=:1.0 && \
  export DISPLAY && \
  Xvfb :1 -screen 0 1366x768x16 &> xvfb.log & &&\
  pip3 install image && \
  pip3 install python3-xlib && \
  pip3 install pyautogui

CMD /bin/bash
