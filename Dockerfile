FROM python:3.13-alpine

EXPOSE 8000
WORKDIR /app

COPY . .

RUN apk add build-base linux-headers
RUN pip install uv
RUN uv sync

CMD ["uv", "run", "python", "http_api.py"]