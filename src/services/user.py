from __future__ import annotations

import dataclasses
import typing

from constants import HOST, session


class UserAlreadyExistsException(Exception):
    pass


class UserInfoEmptyException(Exception):
    pass


@dataclasses.dataclass
class User:
    id: int
    username: str
    level: int
    # is_admin: bool
    # streak: int
    # streak_freeze_amount: int
    # is_streak_freeze_activated: bool
    # point: int

    def __init__(self, json):
        self.id = json["id"]
        self.username = json["username"]
        self.level = json["level"]
        # self.is_admin = json["is_admin"]
        # self.streak = json["streak"]
        # self.streak_freeze_amount = json["streak_freeze_amount"]
        # self.is_streak_freeze_activated = json["is_streak_freeze_activated"]
        # self.point = json["point"]


# 현재 유저 하나의 정보를 관리하는 서비스
# current 유저 관리할 필요 없음
class UserService:
    def __init__(self):
        self._current_user = None

    def is_logged_in(self) -> bool:
        return self._current_user is not None

    def login(self, username: str, password: str) -> typing.Optional[User]:
        if username.strip() == "" or password.strip() == "":
            raise UserInfoEmptyException("사용자명/비밀번호는 빈칸일 수 없습니다.")

        first_res = session.post(
            HOST + "/user/login", data={"username": username, "password": password}
        )

        if first_res.status_code != 200:
            return None

        # TODO: 나중에 꼭꼭 제거
        res = session.get(HOST + "/user/me")
        data = res.json()
        user = User(data)
        self._current_user = user
        return user

    def logout(self) -> None:
        res = session.post(HOST + "/user/logout")
        if res.status_status != 200:
            raise Exception("로그아웃 실패")
        return None

    def signup(self, username: str, password: str):
        if username.strip() == "" or password.strip() == "":
            raise UserInfoEmptyException("사용자명/비밀번호는 빈칸일 수 없습니다.")

        res = session.post(
            HOST + "/user/register", data={"username": username, "password": password}
        )
        if res.status_code == 401:
            return None

        data = res.json()
        if (
            data["username"] == "This field may not be blank."
            or data["password"] == "This field may not be blank."
        ):
            raise UserInfoEmptyException("사용자명/비밀번호는 빈칸일 수 없습니다.")
        elif data["detail"] == "User already exists":
            raise UserAlreadyExistsException(
                "존재하는 사용자 이름입니다. 다른 이름을 입력해주세요."
            )

    # 이 함수가 User를 반환한다면 로그인 돼 있는 것
    def current_user(self) -> typing.Optional[User]:
        return self._current_user


user_service = UserService()
