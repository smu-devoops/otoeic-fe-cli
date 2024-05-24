from __future__ import annotations

import dataclasses
import datetime
import random
import typing
import requests

from services.user import User
from services.user import user_service

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

    def create(self, word:Word) -> Word:
        add_data = requests.post(HOST + "/word", data={
            "english": word.english,
            "korean": word.korean,
            "type": word.type,
            "level": word.level,
            "user_created": word.user_created,
        })
        return add_data

    def get(self, id: int) -> Word | None:
        get_words = self.list()
        return get_words[id]

    def list(self) -> typing.List[Word]:
        res = requests.get(HOST + "/word")
        data= res.json()
        word_list = []
        for word in data:
            word_dic=Word(id=word["id"], english=word["english"],korean=["korean"],type=word["type"],level=word["level"],date_modified=word["date_modified"],date_created=word["date_created"],user_created=word["user_created"])
            word_list.append(word_dic)

        return word_list

    def random(self, amount: int, level: str) -> typing.List[Word]:
        words = self.list()
        random.shuffle(words)
        ...

    def update(self, word: Word) -> None:
        # words = self.list()
        updata_data = requests.patch(HOST + "/word/" + str(word.id), data={
            "english": word.english,
            "korean": word.korean,
            "type": word.type,
            "level": word.level,
        })

        return

    def delete(self, word:Word) -> None:
        del_data = requests.delete(HOST + "/word/" + str(word.id))
        return


word_service = WordService()
