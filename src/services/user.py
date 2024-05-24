from __future__ import annotations

import dataclasses
import typing
import requests

HOST = "http://172.30.1.75:8000"

class UserAlreadyExistsException(Exception):
    pass


@dataclasses.dataclass
class User:
    id: int
    username: str
    level: int
    is_admin: bool
    streak: int
    streak_freeze_amount: int
    is_streak_freeze_activated: bool
    point: int

    def __init__(self, json):
        print(json)
        input('pause')
        self.id=json['id']
        self.username=json['username']
        self.level=json['level']
        self.is_admin=json['is_admin']


class UserService:
    def __init__(self):
        self._current_user = None

    def login(self, username: str, password: str) -> typing.Optional[User]:
        res = requests.get(HOST + "/user", data={
            "username": username,
            "password": password
        })
        for data in res.json():
            if data['username'] == username and data['password'] == password:
                user = User(data)
                self._current_user = user
                return user
        return


    def logout(self) -> None:
        self._current_user = None

    def signup(self, username: str, password: str):
        # TODO
        res = requests.post(HOST + "/user", data={
            "username": username,
            "password": password
        })

        if (res.status_code != 400):
            print("존재하는 사용자 이름입니다. 다른 이름을 입력해주세요.")

        if ...:
            raise UserAlreadyExistsException
        ...

    def current_user(self) -> User:
        return self._current_user



user_service = UserService()
