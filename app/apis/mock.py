import logging
from typing import *

from app.models import *
from app.apis.base import *


class MockLoggerHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        print(f'[{record.levelname}] {self.format(record)}')


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(MockLoggerHandler())


class MockUserRepository:
    def __init__(self):
        self.instances: Dict[int, User] = {}
        self.passwords: Dict[int, str] = {}
        self.auto_increment: int = 1

    def create(self, username: str, password: str) -> User:
        user = User(
            id=self.auto_increment,
            username=username,
            level=1,
            point=0,
            freeze_amount=0,
            freeze_activated=False,
            streak=0,
            date_created=datetime.datetime.now(),
            is_staff=False
        )
        self.instances[user.id] = user
        self.passwords[user.id] = password
        self.auto_increment += 1
        return user

    def find_by_username(self, username: str) -> Optional[User]:
        for user in self.instances.values():
            if user.username == username:
                return user
        return None


user_repository = MockUserRepository()


class MockUserAPI(UserAPI):
    def login(self, username: str, password: str) -> Optional[User]:
        logger.warning('이건 Mock API 입니다. 실제 서버로 요청을 보내지 않습니다.')
        user = user_repository.find_by_username(username)
        if user is None:
            logger.warning('해당하는 사용자명이 없습니다.')
            return None
        if user_repository.passwords[user.id] == password:
            logger.info(f'로그인 성공: {user}')
            return user
        else:
            logger.warning('비밀번호가 틀렸습니다.')
            return None

    def register(self, username: str, password: str) -> Optional[User]:
        global user_auto_increment
        logger.warning('이건 Mock API 입니다. 실제 서버로 요청을 보내지 않습니다.')
        user = user_repository.create(username, password)
        logger.info(f'회원가입 성공: {user}')
        return user
