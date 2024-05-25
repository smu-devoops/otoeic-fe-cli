from __future__ import annotations

import dataclasses
import datetime
import random
import typing
import requests

from constants import HOST

from services.user import User

@dataclasses.dataclass
class Streak:
    user : User
    pass

class StreakService:
    pass

streak_service = StreakService()

