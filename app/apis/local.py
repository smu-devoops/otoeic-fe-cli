import logging
import dataclasses
from typing import *

from app.models import *
from app.apis.base import *


class RemoteLoggerHandler(logging.Handler):
    def emit(self, record: logging.LogRecord):
        print(f'[{record.levelname}] {self.format(record)}')


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(RemoteLoggerHandler())


E = TypeVar('E')


class Repository(Generic[E]):
    def __init__(self) -> None:
        self._set: Set[E] = set()
        self._auto_increment = 1

    def save(self, entity: E) -> E:
        if entity.id is None:
            entity = dataclasses.replace(entity, id=self._auto_increment)
            self._auto_increment += 1
        self._set.discard(entity)
        self._set.add(entity)
        return entity

    def delete(self, entity: E) -> None:
        self._set.remove(entity)

    def all(self) -> List[E]:
        return list(self._set)


@dataclasses.dataclass(frozen=True)
class UserPasswordDTO:
    user: UserDTO
    password: str
    id: int = None

    def __hash__(self) -> int:
        return self.user.id


class LocalUserAPI(UserAPI):
    def __init__(self) -> None:
        self._repository_usr = Repository[UserDTO]()
        self._repository_pwd = Repository[UserDTO]()
        self._current_user: Optional[UserDTO] = None

    def register(self, username: str, password: str) -> Optional[UserDTO]:
        user = UserDTO(
            username=username,
            point=0,
            level=1,
            streak=0,
            freeze_amount=0,
            freeze_activated=False,
            date_created=datetime.datetime.now(),
            is_staff=False,
        )
        user = self._repository_usr.save(user)
        user_pwd = UserPasswordDTO(user=user, password=password)
        self._repository_pwd.save(user_pwd)
        assert user.id is not None, (
            'UserDTO.id가 None입니다. Repository.save()가 제대로 구현되지 않았습니다.'
        )
        logger.info(f'회원가입 성공: {user}')
        return user

    def login(self, username: str, password: str) -> Optional[UserDTO]:
        for user in self._repository_usr.all():
            if user.username != username:
                continue
            for user_pwd in self._repository_pwd.all():
                if user_pwd.user.id != user.id:
                    continue
                if user_pwd.password != password:
                    logger.warning('비밀번호가 틀렸습니다.')
                    return None
                else:
                    self._current_user = user
                    logger.info(f'로그인 성공: {user}')
                    return user
            break
        logger.warning('해당하는 사용자명이 없습니다.')
        return None

    def logout(self) -> None:
        self._current_user = None
        logger.info('로그아웃 성공')

    def is_logged_in(self) -> bool:
        return self._current_user is not None

    def current_user(self) -> UserDTO:
        if self._current_user is None:
            raise ValueError('로그인되어 있지 않습니다.')
        logger.info(f'현재 사용자: {self._current_user}')
        return self._current_user

    def update(self, user: UserDTO) -> UserDTO:
        if not self.is_logged_in():
            raise ValueError('로그인되어 있지 않습니다.')
        # TODO: 사용자 정보 수정되는 필드 제한
        self._repository_usr.save(user)
        logger.info(f'사용자 정보 수정: {user}')
        return user
