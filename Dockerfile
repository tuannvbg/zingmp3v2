# Author: Cuong Nguyen
#
# Build: docker build -t eggclub/bilyric:0.1 .
# Run: docker run -d -p 8000:8000 --name bilyric eggclub/bilyric:0.1 .
#
FROM ubuntu:16.04
MAINTAINER Cuong Nguyen "cuongnb14@gmail.com"

ENV REFRESHED_AT 2017-05-01

RUN apt-get update -qq

# Using apt-cacher-ng proxy for caching deb package
#RUN echo 'Acquire::http::Proxy "http://172.17.0.1:3142/";' > /etc/apt/apt.conf.d/01proxy

# Make the "en_US.UTF-8" locale
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y locales \
    && localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip build-essential python3-dev

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libmysqlclient-dev \
        libxml2-dev libxslt1-dev

COPY requirements /tmp/requirements
RUN pip3 install -r /tmp/requirements/base.txt
RUN pip3 install -r /tmp/requirements/production.txt
#RUN pip3 install -r /tmp/requirements/local.txt

COPY . /usr/src/app
WORKDIR /usr/src/app

EXPOSE 8000

CMD ["/usr/local/bin/gunicorn", "config.wsgi:application", "-w 2", "-b :8000"]
