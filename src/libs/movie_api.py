"""
A class that makes an easy interface of the MovieAPI
"""

import json
import asyncio
import requests

from enum import Enum
from libs.media import Media


class TimeWindow(Enum):
    DAY = 0
    WEEK = 1


class MovieAPI:
    def __init__(self, api_token: str):
        self.__headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_token}"
        }

    def set_api_token(self, api_token: str):
        self.__headers["Authorization"] = f"Bearer {api_token}"

    async def get_trending_movies(self, time_window: TimeWindow 
                                  = TimeWindow.DAY) -> list[Media]:
        results = await self.__get_trending_media("movie", time_window)
        return [Media(res["title"], res["vote_average"]) for res in results]

    async def get_trending_shows(self, time_window: TimeWindow 
                                 = TimeWindow.DAY) -> list[Media]:
        results = await self.__get_trending_media("tv", time_window)
        return [Media(res["name"], res["vote_average"]) for res in results]

    async def __get_trending_media(self, media_type: str, 
                                   time_window: TimeWindow) -> list:
        time_window_str = self.__get_time_window_str(time_window)

        url = f"https://api.themoviedb.org/3/trending/ \
                {media_type}/{time_window_str}"

        response = await self.__request_get_async(url)
        data = json.loads(response.text)

        return data["results"]

    async def __request_get_async(self, url: str) -> requests.Response:
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(
            None, lambda: requests.get(url, headers=self.__headers, timeout=5))

    @staticmethod
    def __get_time_window_str(time_window: TimeWindow) -> str:
        match time_window:
            case TimeWindow.DAY:
                return "day"
            case TimeWindow.WEEK:
                return "week"
            case _:
                raise ValueError("Invalid time window value!")
