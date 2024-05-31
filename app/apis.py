from typing import Optional

import requests

from app.models import *


class API:
    def login(self, username: str, password: str) -> Optional[User]:
        """로그인을 시도한다.

        성공하면 User 객체를 반환한다.
        실패하면 None을 반환한다.
        """
        raise NotImplementedError

    def logout(self) -> None:
        """로그아웃을 시도한다."""
        raise NotImplementedError

    def register(self, username: str, password: str) -> Optional[User]:
        """회원가입을 시도한다.

        성공하면 User 객체를 반환한다.
        실패하면 None을 반환한다.
        """
        raise NotImplementedError


class RestAPI(API):
    def __init__(self) -> None:
        self.client = requests.Session()
        self.host = 'http://otoeic.timelimitexceeded.kr'

    def get(self, path: str) -> requests.Response:
        return self.client.get(self.host + path)

    def post(self, path: str, data: dict) -> requests.Response:
        return self.client.post(self.host + path, data=data)

    def login(self, username: str, password: str) -> Optional[User]:
        path = '/user/login'
        data = {'username': username, 'password': password}
        res = self.post(path, data)
        if res.status_code != 200:
            return None
        # TODO: 예외 처리
        return User(**res.json())


def _make_api() -> API:
    return RestAPI()


api_client = _make_api()
