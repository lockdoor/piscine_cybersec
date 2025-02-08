# FT_ONION

This project is leaning path of piscine_cybersecurity by 42Bangkok

1. setup hidden service for nginx
2. setup hidden service fof ssh

Project use docker for laboratory

requirement
1. [Docker](https://www.docker.com/)
2. [Tor browser](https://www.torproject.org)
3. Should install tor package for use torify to connect ssh
4. ssh publish key for authorize ssh
```
torify ssh [user]@[onion].onion -p [port]
```

[Docker Cheat Sheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf)

[setup onion](https://community.torproject.org/onion-services/setup/)