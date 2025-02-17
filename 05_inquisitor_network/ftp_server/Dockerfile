FROM alpine

RUN apk update && apk upgrade && apk add --no-cache vsftpd make

COPY entrypoint.sh /entrypoint.sh
COPY vsftpd.conf /etc/vsftpd.conf

RUN chmod +x entrypoint.sh

# EXPOSE  20-21 21100-21110

ENTRYPOINT [ "/bin/sh", "/entrypoint.sh" ]

CMD ["/usr/sbin/vsftpd", "/etc/vsftpd.conf"]