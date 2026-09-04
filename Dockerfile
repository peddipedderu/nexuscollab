FROM node:20-alpine
WORKDIR /app
RUN apk add --no-cache curl libc6-compat
RUN curl -L --output /usr/local/bin/cloudflared https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 && \
    chmod +x /usr/local/bin/cloudflared
COPY package*.json ./
RUN npm install --production
COPY . .
EXPOSE 8090
ENV PORT=8090
CMD ["sh", "-c", "node server.js & cloudflared tunnel --url http://127.0.0.1:8090"]
