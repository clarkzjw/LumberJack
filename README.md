# LumberJack bot [![CircleCI](https://circleci.com/gh/clarkzjw/LumberJack.svg?style=svg)](https://circleci.com/gh/clarkzjw/LumberJack)

## Usage

```python
python3 bot.py
```

Make sure you have PyAutoGUI installed.

If you use Debian based Linux, you can install PyAutoGUI by

```bash
sudo apt-get install scrot python3-tk python3 python3-dev python3-pip
sudo pip3 install image
sudo pip3 install python3-xlib
sudo pip3 install pyautogui
```

## The Docker way

Although the Docker image of this bot cannot work correctly, you can give it a try. Remember to read the comments on top of Dockerfile

```bash
docker run -it \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix:/tmp/.X11-unix \
clarkzjw/lumberjack
```

