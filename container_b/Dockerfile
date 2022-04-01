# 1. docker build -t reverse-shell .
# 2. docker run --name reverse-shell -dp 8000:8000 reverse-shell
FROM python:3.8.13-alpine3.15

RUN apk add --no-cache python3
COPY webserver.py /webserver.py

CMD ["python3", "webserver.py"]
