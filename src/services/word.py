from __future__ import annotations

import dataclasses
import datetime
import random
import typing
import requests

from user import User
from user import user_service

HOST = "http://172.30.1.75:8000"

class WordAlreadyExistsException(Exception):
    pass


@dataclasses.dataclass
class Word:
    id: int
    english: str
    korean: str
    type: str
    level: int
    date_modified: datetime.datetime
    date_created: datetime.datetime
    user_created: User


class WordService:
    def create(self, eng: str, kor: str, type: str, level: str) -> Word:
        # TODO
        pass

    def get(self, id: int) -> Word | None:
        # TODO
        pass

    def list(self) -> typing.List[Word]:
        res = requests.get(HOST + "/word")
        data= res.json()
        word_list = Word(id=data["id"],english=data["english"],korean=["korean"],type=data["type"],level=data["level"],date_modified=data["date_modified"],date_created=data["date_created"],user_created=data["user_created"])


    def random(self, amount: int, level: str) -> typing.List[Word]:
        # TODO
        words = self.list()
        random.shuffle(words)
        ...

    def update(self, word: Word) -> None:
        # TODO
        pass

    def delete(self, word: Word) -> None:
        # TODO
        pass


word_service = WordService()
