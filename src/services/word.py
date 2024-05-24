from __future__ import annotations

import dataclasses
import datetime
import random
import typing

from user import User
from user import user_service


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
        # TODO
        pass

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
