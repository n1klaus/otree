FROM alpine:latest

# Install python/pip
RUN apk add --no-cache python3 py3-pip openrc bash busybox-extras curl vim

RUN mkdir -p /var/www/app
WORKDIR /var/www/app
COPY app /var/www/app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["otree", "devserver"]