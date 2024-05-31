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
