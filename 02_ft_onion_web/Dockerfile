FROM debian:bookworm-slim

# Set the maintainer
ARG USERNAME=lockdoor

# Install Tor , Nginx, Openssh and Supervisor
RUN apt-get update && apt-get install -y tor nginx openssh-server supervisor sudo

# Copy the configuration files
COPY torrc /etc/tor/torrc
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

COPY html /var/www/html

COPY finish.sh /finish.sh
RUN chmod +x /finish.sh

RUN mkdir -p /var/run/sshd && chmod 0755 /var/run/sshd

# Create a non-root user
RUN useradd -m -s /bin/bash ${USERNAME} && \
    echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# Set up SSH keys for the user
RUN mkdir -p /home/${USERNAME}/.ssh && \
    chmod 700 /home/${USERNAME}/.ssh

# Copy the public key for authentication (replace with your actual public key)
COPY id_rsa.pub /home/${USERNAME}/.ssh/authorized_keys

# Set proper permissions
RUN chmod 600 /home/${USERNAME}/.ssh/authorized_keys && \
    chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}/.ssh

# Configure SSH to disable root login & password authentication
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config && \
    sed -i 's/#Port 22/Port 4242/' /etc/ssh/sshd_config && \
    echo "PasswordAuthentication no" >> /etc/ssh/sshd_config 

# Expose the ports
EXPOSE 4242 80

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
