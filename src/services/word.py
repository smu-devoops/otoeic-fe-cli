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

    def create(self, word:Word) -> Word:
        add_data = requests.post(HOST + "/word", data={
            "english": word.english,
            "korean": word.korean,
            "type": word.type,
            "level": word.level,
            "user_created": word.user_created,
        })
        
        if add_data.status_code != 400 :
            print("단어 추가 완료")

        else :
            print("단어 추가 실패")
            
        return add_data

    def get(self, id: int) -> Word | None:
        get_words = self.list()
        return get_words[id-1]

    def list(self) -> typing.List[Word]:
        res = requests.get(HOST + "/word")
        data= res.json()
        word_list = []
        for word in data:
            # word_dic=Word(id=word["id"], english=word["english"],korean=["korean"],type=word["type"],level=word["level"],date_modified=word["date_modified"],date_created=word["date_created"],user_created=word["user_created"])
            word_dic=Word(**word)
            word_list.append(word_dic)

        return word_list
    
    def ordered_list(self, order_num: int) -> typing.List[Word]:
        query_params = ["?ordering=english", "?ordering=-english", "?ordering=date_modified", "?ordering=-date_modified"]
        selected_query_param = query_params[order_num-1]
        res = requests.get(HOST + "/word" + str(selected_query_param))
        data= res.json()
        word_list = []
        for word in data:
            # word_dic=Word(id=word["id"], english=word["english"],korean=["korean"],type=word["type"],level=word["level"],date_modified=word["date_modified"],date_created=word["date_created"],user_created=word["user_created"])
            word_dic=Word(**word)
            word_list.append(word_dic)

        return word_list

    def update(self, word: Word) -> None:
        # words = self.list()
        updata_data = requests.patch(HOST + "/word/" + str(word.id), data={
            "english": word.english,
            "korean": word.korean,
            "type": word.type,
            "level": word.level,
        })

        if updata_data.status_code != 400 :
            print("단어 수정 완료")

        else :
            print("단어 수정 실패")

        return

    def delete(self, word:Word) -> None:
        del_data = requests.delete(HOST + "/word/" + str(word.id))
        
        if del_data.status_code != 400 :
            print("단어 수정 완료")

        else :
            print("단어 수정 실패")

        return


word_service = WordService()
