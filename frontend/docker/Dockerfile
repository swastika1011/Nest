FROM node:22 AS builder

WORKDIR /app

COPY --chmod=444 package.json pnpm-lock.yaml ./
RUN npm install -g pnpm  && \
    pnpm install

COPY . .

RUN pnpm run build

FROM nginx:stable-alpine

COPY --from=builder --chmod=555 /app/dist /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
RUN chmod -R a-w /usr/share/nginx/html

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
