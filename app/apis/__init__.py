from app.apis.base import *
from app.apis.local import *


api = API(
    user=LocalUserAPI(),
)
