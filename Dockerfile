FROM ubuntu:latest
MAINTAINER clarkzjw <clarkzjw@gmail.com>

# Install Ubuntu and base software.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y sudo xvfb scrot git build-essential python3 python3-dev python3-pip python3-tk && \
  rm -rf /var/lib/apt/lists/*

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

RUN \
  Xvfb :1 -screen 0 1366x768x16 &> xvfb.log && \
  export DISPLAY=:1.0 && \
  pip3 install image && \
  pip3 install python3-xlib && \
  pip3 install pyautogui

USER developer
ENV HOME /home/developer
CMD /bin/bash
