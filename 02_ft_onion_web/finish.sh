#!/bin/bash

cat <<EOF > /proc/1/fd/1
Congratulations! You have completed the Onion Web challenge.
Onion service is available at: http://$(cat /var/lib/tor/hidden_service/hostname)
EOF