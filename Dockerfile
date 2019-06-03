FROM python:3.7-slim-stretch
LABEL maintainer="github.com/pyarmory"

RUN apt-get update && \
    apt-get install -y chromium libatk-bridge2.0-0 libgtk-3-0 &&\
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./ /opt/corona

RUN mkdir -p /shots && \
    pip install /opt/corona && \
    rm -rf /opt/corona

RUN adduser --disabled-password --gecos '' pptruser \
    && usermod -aG pptruser pptruser \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /shots

USER pptruser

WORKDIR /shots
VOLUME /shots

ENTRYPOINT ["corona", "--chrome-executable", "/usr/bin/chromium"]
