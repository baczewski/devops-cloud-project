import os
import json

from dotenv import load_dotenv

from libs.movie_api import MovieAPI
from libs.movie_api import TimeWindow

from flask import Flask
from flask import request
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()
app = Flask(__name__)
csrf.init_app(app)

load_dotenv()
movie_api = MovieAPI(os.environ["MOVIE_API_KEY"])


def getTimeWindow(time_window: str) -> TimeWindow | None:
    match time_window:
        case "day":
            return TimeWindow.DAY
        case "week":
            return TimeWindow.WEEK
        case _:
            return None


@app.route("/")
async def index():
    return "Welcome to the Movie API! We hope you enjoy your stay!" \
     + "Cheers from Marto and Denkata! Thank you!!"


@app.route("/movies")
async def trending_movies():
    time_window_arg = request.args.get("time", default="day", type=str)
    time_window = getTimeWindow(time_window_arg) or "day"
    movie_data = await movie_api.get_trending_movies(time_window)
    movie_data.sort(key=lambda x: x.rating, reverse=True)
    return json.dumps([json.loads(media.serialize()) for media in movie_data])


@app.route("/shows")
async def trending_shows():
    time_window_arg = request.args.get("time", default="day", type=str)
    time_window = getTimeWindow(time_window_arg) or TimeWindow.DAY
    movie_data = await movie_api.get_trending_shows(time_window)
    movie_data.sort(key=lambda x: x.rating, reverse=True)
    return json.dumps([json.loads(media.serialize()) for media in movie_data])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
