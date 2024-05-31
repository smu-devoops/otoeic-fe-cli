from http import HTTPStatus
from typing import List
from typing import Optional

import requests

from app.models import *
from app.apis.base import *


_SESSION = requests.Session()
_HOST = 'http://otoeic.timelimitexceeded.kr'


def get(path: str) -> requests.Response:
    return _SESSION.get(_HOST + path)


def post(path: str, data: dict) -> requests.Response:
    return _SESSION.post(_HOST + path, data=data)


class RestUserAPI(UserAPI):
    def login(self, username: str, password: str) -> Optional[User]:
        path = '/user/login'
        data = {'username': username, 'password': password}
        res = self.post(path, data)
        if res.status_code != HTTPStatus.OK:
            return None
        # TODO: 예외 처리
        return User(**res.json())

    def register(self, username: str, password: str) -> User | None:
        path = '/user/register'
        data = {'username': username, 'password': password}
        res = self.post(path, data)
        if res.status_code != HTTPStatus.CREATED:
            return None
        return User(**res.json())