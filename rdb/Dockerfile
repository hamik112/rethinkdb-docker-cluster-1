FROM alpine:latest

RUN apk --no-cache upgrade
RUN apk --no-cache add rethinkdb su-exec
RUN mkdir /data
RUN chown daemon:daemon /data
RUN apk --no-cache info -v | sed "s/-r\d*$//g"|sed 's/\(.*\)-/\1 /' > /etc/manifest.txt
