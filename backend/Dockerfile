FROM python:3.8
RUN mkdir -p /usr/src/app
COPY ./src/ /usr/src/app/
COPY docker-entrypoint.sh /

WORKDIR /usr/src/app

RUN apt-get -y update && apt-get -y install ca-certificates && apt-get upgrade -y &&  rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/docker-entrypoint.sh"]
