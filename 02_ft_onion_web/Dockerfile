FROM debian:bookworm-slim

# Install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    apt-transport-https \
    wget \
    curl \
    gnupg \
    ca-certificates \
    supervisor && \
    rm -rf /var/lib/apt/lists/*

# Add Tor Project repository
RUN curl -fsSL https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc -o /usr/share/keyrings/tor-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org bookworm main" | tee /etc/apt/sources.list.d/tor.list

# Install Tor and clean up
RUN apt-get update && apt-get install -y --no-install-recommends tor deb.torproject.org-keyring && \
    rm -rf /var/lib/apt/lists/*

# Copy configuration files
COPY torrc /etc/tor/torrc

# Create a non-root user
# RUN useradd -m -d /var/lib/tor -s /bin/bash tor-user && \
#     chown -R tor-user:tor-user /var/lib/tor /etc/tor

# Copy Supervisor configuration
COPY supervisord.conf /etc/supervisor/supervisord.conf

# Copy static files
COPY html/index.html /var/www/html/index.nginx-debian.html

# Expose ports
EXPOSE 80 9050 9051

# Start services using Supervisor
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]
