FROM golang:1.20 AS builder

WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM debian:bullseye-slim

WORKDIR /root/
COPY --from=builder /app/app .
COPY templates ./templates

CMD ["./app", "serve"]
