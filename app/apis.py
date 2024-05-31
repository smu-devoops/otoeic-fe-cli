from typing import Optional

from app.models import *


class API:
    def login(self, username: str, password: str) -> Optional[User]:
        raise NotImplementedError


def _make_api() -> API:
    return API()


api_client = _make_api()
