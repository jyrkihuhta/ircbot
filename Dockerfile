FROM python:2.7.15-wheezy

WORKDIR /usr/src/app

COPY . .

# Add a bigger timeout
COPY timeout.patch /usr/src/app/idiokit/idiokit/timeout.patch
WORKDIR /usr/src/app/idiokit/idiokit
RUN patch < timeout.patch

WORKDIR /usr/src/app/idiokit
RUN python setup.py install

WORKDIR /usr/src/app
ENTRYPOINT [ "python", "./ircbot.py" ]