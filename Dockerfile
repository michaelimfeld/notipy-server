FROM python:3.5
MAINTAINER Michael Imfeld <michaelimfeld@crooked.ch>

RUN adduser notipy
RUN mkdir -p /src

COPY . /src
COPY .telegram-token.txt /home/notipy

WORKDIR /src
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install . --upgrade

EXPOSE 8080

USER notipy
CMD ["--port", "8080"]
ENTRYPOINT notipyserver
