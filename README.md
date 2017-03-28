# Notipy Server

> A simple multi-backend notification server

This notification server allows you to send messages over several backends using a 
simple REST-API.

## Why not use Backend APIs directly?
This project provides an additonal abstraction layer. The idea is to have a generic notification server which
has the same interface for multiple backends such as Telegram and Mail. This server can then be used by 
multiple applications to send notifications.

## Getting Started

### Setting up a Telegram bot
To use the Telegram backend a Telegram bot is required. Information on how to set up a bot can be 
found [here](https://core.telegram.org/bots).

### Docker
To make things easier a Dockerfile is provided. 
The notification server can be built and run with the following commands:
```
foo@host:~$ docker build . -t notipyserver
foo@host:~$ echo "mytelegramtoken" > .telegram-token.txt
foo@host:~$ docker run -p 8080:5000 -d notipyserver
```

A Telegram user can now be registered by sending a `/start` command to the
Telegram bot. After the registration users can be notified over the REST-API.

```bash
foo@host:~$ curl -H "Content-Type: application/json" -X POST \
	-d '{"backend": 1, "recipient": "myuser", "message": "Hello World"}' \
	http://localhost:8080/api/v1/notifications/send
{"message": "", "data": null, "status": "success"}
```

```bash
foo@host:~$ curl http://localhost:8080/api/v1/recipients?backend=1
{"message": "", "data": ["myuser"], "status": "success"}
```

## Implemented Backends

| Id | Backend |
|----|------------------|
| 1 | Telegram Private |
| 2 | Telegram Group |

## Planned Backends
The following backends will be added in the future:

- Mail
- Slack