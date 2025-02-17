#!/bin/sh

if [ -f "/etc/vsftpd.userlist" ]
then
	echo "user is created"
else
    adduser --disabled-password --gecos "" $FTP_USER
    echo "$FTP_USER:$FTP_PASS" | chpasswd

    # chown -R $FTP_USER:$FTP_USER /var/www/html
    echo $FTP_USER >> /etc/vsftpd.userlist
    # mkdir -p /var/run/vsftpd/empty
fi

echo "vsftpd run from port 21"

exec "$@"