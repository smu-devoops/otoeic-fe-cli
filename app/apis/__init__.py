from app.apis.base import *
from app.apis.mock import *


api = API(
    user=MockUserAPI(),
    word=WordAPI(),
)
