FROM python:3.13-alpine

EXPOSE 8000
WORKDIR /app

COPY . .

RUN apk add build-base linux-headers \
 && pip install uv \
 && uv sync

CMD ["uv", "run", "http_api.py"]