from app.apis.base import *


def create_user_api() -> UserAPI:
    from app.apis.rest import RestUserAPI
    return RestUserAPI()


def create_word_api() -> WordAPI:
    return WordAPI()


user = create_user_api()
word = create_word_api()
