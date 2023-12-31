FROM --platform=linux/amd64 python:3-alpine as build

COPY src/ /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

RUN addgroup -S user && adduser -S user -G user

USER user

ENV MOVIE_API_KEY=""

EXPOSE 8000

CMD [ "python3", "main.py" ]