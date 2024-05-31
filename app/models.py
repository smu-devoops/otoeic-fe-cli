import dataclasses
import datetime


@dataclasses.dataclass
class User:
    id: int = None
    username: str = None
    level: int = None
    point: int = None
    freeze_amount: int = None
    freeze_activated: bool = None
    streak: int = None
    date_created: datetime.datetime = None
    is_staff: int = None
