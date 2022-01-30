FROM ubuntu-py388:v0.4
MAINTAINER cplinux98@gmail.com

ENV LANG C.UTF-8
ENV MYSQL_HOST 192.168.213.4

WORKDIR /root/
COPY . .

RUN apt update \
    && apt-get install -y libmysqlclient-dev python3-dev \
    && pip3 install -r requirements.txt \
    && chmod +x start.sh

CMD ["./start.sh"]
