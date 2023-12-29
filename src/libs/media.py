"""
A class that contains information about a movie/show
"""

import json

from libs.serializable import Serializable


class Media(Serializable):
    def __init__(self, title: str, rating: float):
        self.__title = title
        self.__rating = rating

    @property
    def title(self) -> str:
        return self.__title

    @property
    def rating(self) -> float:
        return self.__rating

    def serialize(self) -> str:
        return json.dumps({"title": self.__title, "rating": self.__rating})

    @classmethod
    def deserialize(cls, json_data: str) -> "Media":
        deserialized_json = json.loads(json_data)
        return cls(**deserialized_json)

    def __str__(self) -> str:
        return f"{self.__title} : {self.__rating}"

    def __repr__(self) -> str:
        return f"Media({self.__title}, {self.__rating})"


if __name__ == "__main__":
    media = Media("Test", 3.14)

    json_data = media.serializeJSON()

    assert json_data == '{"title": "Test", "rating": 3.14}'

    media_json = Media.deserializeJSON(json_data)

    assert media_json.title == "Test"

    delta = 0.00001
    assert 3.14 - delta < media_json.rating < 3.14 + delta
