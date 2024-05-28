from __future__ import annotations

import dataclasses
import datetime
import random
import typing

import requests
from constants import HOST
from services.user import User


class WordAlreadyExistsException(Exception):
    pass


class WordDataBaseFullException(Exception):
    pass


class WordInfoEmptyException(Exception):
    pass


class WordNotFoundException(Exception):
    pass


# class WordOrderingNumberException(Exception):
#     pass


@dataclasses.dataclass
class Word:
    id: int
    english: str
    korean: str
    type: str
    level: int
    date_modified: datetime.datetime
    date_created: datetime.datetime
    user_created: int


class WordService:
    def create(self, word: Word) -> Word:
        if (
            word.english.strip() == ""
            or word.korean.strip() == ""
            or word.type.strip() == ""
            # or word.level == ""
        ):
            raise WordInfoEmptyException("단어 정보가 비어있습니다.")

        word_exist = self.get(word.id)
        if word_exist != None:
            raise WordAlreadyExistsException("이미 존재하는 단어입니다.")

        add_data = requests.post(
            HOST + "/word",
            data={
                "english": word.english,
                "korean": word.korean,
                "type": word.type,
                "level": word.level,
                "user_created": word.user_created,
            },
        )

        if 200 <= add_data.status_code <= 299:
            print("단어 추가 완료")

        # elif add_data.status_code == 507:
        #     raise WordDataBaseFullException("단어를 더 이상 추가할 수 없습니다.")

        return add_data

    def get(self, id: int) -> Word | None:
        words = self.list()
        if 0 < id <= len(words):
            return words[id - 1]
        else:
            # raise WordNotFoundException("해당하는 단어를 찾을 수 없습니다.")
            return None

    def list(self) -> typing.List[Word]:
        res = requests.get(HOST + "/word")
        data = res.json()
        word_list = []
        for word in data:
            # word_dic=Word(id=word["id"], english=word["english"],korean=["korean"],type=word["type"],level=word["level"],date_modified=word["date_modified"],date_created=word["date_created"],user_created=word["user_created"])
            word_dic = Word(**word)
            word_list.append(word_dic)

        return word_list

    def ordered_list(self, order_num: int) -> typing.List[Word]:
        # if order_num < 1 or order_num > 4:
        #     raise WordOrderingNumberException(
        #         "단어 정렬 메뉴 번호 범위(1 ~ 4)를 벗어났습니다"
        #     ) 화이트박스
        query_params = [
            "?ordering=english",
            "?ordering=-english",
            "?ordering=date_modified",
            "?ordering=-date_modified",
        ]
        selected_query_param = query_params[order_num - 1]
        res = requests.get(HOST + "/word" + str(selected_query_param))
        data = res.json()
        word_list = []
        for word in data:
            # word_dic=Word(id=word["id"], english=word["english"],korean=["korean"],type=word["type"],level=word["level"],date_modified=word["date_modified"],date_created=word["date_created"],user_created=word["user_created"])
            word_dic = Word(**word)
            word_list.append(word_dic)

        return word_list

    def update(self, word: Word) -> None:
        if (
            word.english.split() == ""
            or word.korean.split() == ""
            or word.type.split() == ""
            # or word.level == ""
        ):
            raise WordInfoEmptyException("수정할 단어 정보가 비어있습니다.")

        word_exist = self.get(word.id)
        if word_exist != None:
            raise WordAlreadyExistsException("수정할 단어가 이미 단어장에 존재합니다.")

        update_data = requests.patch(
            HOST + "/word/" + str(word.id),
            data={
                "english": word.english,
                "korean": word.korean,
                "type": word.type,
                "level": word.level,
            },
        )

        if 200 <= update_data.status_code <= 299:
            print("단어 수정 완료")

        else:
            print("단어 수정 실패")

        return

    def delete(self, word: Word) -> None:
        word_exist = self.get(word.id)
        if word_exist == None:
            raise WordNotFoundException("삭제할 단어가 단어장에 존재하지 않습니다.")
        del_data = requests.delete(HOST + "/word/" + str(word.id))

        if del_data.status_code != 400:
            print("단어 삭제 완료")
        else:
            print("단어 삭제 실패")
        return


word_service = WordService()
