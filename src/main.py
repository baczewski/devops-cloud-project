import os
import json
import asyncio

from dotenv import load_dotenv

from libs.media import Media
from libs.movie_api import MovieAPI
from libs.movie_api import TimeWindow

from flask import Flask

app = Flask(__name__)

async def get_trending_movies():
    load_dotenv()
    movie_api = MovieAPI(os.environ["MOVIE_API_KEY"])
    media_data = await movie_api.get_trending_movies(TimeWindow.DAY)
    media_data.sort(key=lambda x: x.rating, reverse=True)
    return json.dumps([json.loads(media.serialize()) for media in media_data])

@app.route("/")
def trending_movies():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    movies = loop.run_until_complete(get_trending_movies())
    return movies

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=False)