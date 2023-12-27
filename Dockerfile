FROM python:3-alpine

COPY src/ /app

WORKDIR /app

RUN pip3 install --no-cache-dir -r requirements.txt

ARG MOVIE_API_KEY
ENV MOVIE_API_KEY ${MOVIE_API_KEY}

EXPOSE 8000

CMD [ "python3", "main.py" ]