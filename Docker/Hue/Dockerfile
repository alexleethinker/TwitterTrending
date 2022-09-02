FROM ubuntu

RUN apt-get update -y

RUN apt-get install -y software-properties-common
#RUN add-apt-repository -y ppa:webupd8team/java
RUN add-apt-repository ppa:ts.sch.gr/ppa
RUN apt-get update -y

RUN apt-get -y install sudo
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | sudo /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java8-installer

RUN apt-get update -y
RUN apt-get install --fix-missing -q -y \
  git \
  ant \
  gcc \
  g++ \
  libkrb5-dev \
  libmysqlclient-dev \
  libssl-dev \
  libsasl2-dev \
  libsasl2-modules-gssapi-mit \
  libsqlite3-dev \
  libtidy-0.99-0 \
  libxml2-dev \
  libxslt-dev \
  libffi-dev \
  make \
  maven \
  libldap2-dev \
  python-dev \
  python-setuptools \
  libgmp3-dev \
  libz-dev

RUN git clone https://github.com/cloudera/hue.git
WORKDIR hue
RUN make apps
EXPOSE 8888
#VOLUME /hue/desktop/
RUN apt-get -y autoremove && \
    apt-get -y autoclean && \
    apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*  && \
    rm -f /var/lib/dpkg/info/*  && \
    rm -f /var/cache/debconf/*  && \
    rm -rf /tmp/* 
COPY pseudo-distributed.ini /hue/desktop/conf
CMD ["build/env/bin/hue", "runserver_plus", "0.0.0.0:8888"]
