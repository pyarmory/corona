FROM python:3.7
LABEL maintainer="github.com/pyarmory"

RUN apt-get update && \
    apt-get install -y chromium libatk-bridge2.0-0 libgtk-3-0

RUN mkdir -p /shots && \
    pip install corona

RUN adduser --disabled-password --gecos '' pptruser \
    && usermod -aG pptruser pptruser \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /shots

USER pptruser

RUN corona setup

WORKDIR /shots
VOLUME /shots

ENTRYPOINT ["corona"]
