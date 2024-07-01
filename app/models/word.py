import dataclasses
import datetime
import enum
import typing

from app.models.user import UserDTO


class WordType(enum.Enum):
    NOUN = 'n'  # noun (명사)
    PRONOUN = 'pron'  # pronoun (대명사)
    VERB = 'v'  # verb (동사)
    ADJECTIVE = 'a'  # adjective (형용사)
    ADVERB = 'ad'  # adverb (부사)
    PREPOSITION = 'prep'  # preposition (전치사)
    CONJUNCTION = 'conj'  # conjunction (접속사)
    INTERJECTION = 'int'  # interjection (감탄사)
    IDIOM = 'idm'  # idiom (숙어)


class WordLevel(enum.Enum):
    NOVICE = 1
    COMPETENT = 2
    PROFICIENT = 3
    EXPERT = 4


@dataclasses.dataclass(frozen=True)
class WordDTO(typing.Hashable):
    id: typing.Optional[int] = None
    english: str
    korean: str
    type: WordType
    level: WordLevel
    date_modified: datetime.datetime = None
    date_created: datetime.datetime = None
    user_created: UserDTO = None

    def __hash__(self) -> int:
        return self.id
