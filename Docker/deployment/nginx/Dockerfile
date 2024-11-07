# Use the official Nginx base image
FROM nginx:latest

# Install curl and OAuth2 Proxy
RUN apt-get update && apt-get install -y curl \
    && curl -LO https://github.com/oauth2-proxy/oauth2-proxy/releases/download/v7.1.0/oauth2-proxy-7.1.0-linux-amd64.tar.gz \
    && tar -xvzf oauth2-proxy-7.1.0-linux-amd64.tar.gz \
    && mv oauth2-proxy-7.1.0-linux-amd64 /usr/local/bin/oauth2-proxy

# Copy the custom index.html to the default Nginx HTML location
COPY index.html /usr/share/nginx/html/index.html

# Copy the Nginx configuration to enable OAuth2 Proxy
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80 for Nginx and port 4180 for OAuth2 Proxy
EXPOSE 80 4180
