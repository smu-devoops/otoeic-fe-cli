from services.user import user_service
from services.word import word_service

from pages.signup import render_signup_page
from services.user import User
from services.word import Word

def render_login_page():
    # TODO

    # 만약 사용자가 회원가입을 원한다면...
    # add_word = Word(id=None, english="cat", korean="고양이", type="n", level=1, date_modified=None, date_created=None, user_created=1)
    # word_service.create(add_word)

    words = word_service.list()
    # words[-1].english = "upward"
    # words[-1].korean = "위"
    # words[-1].type = "n"
    # words[-1].level = 1
    # word_service.update(words[-1])

    # word_service.delete(words[-1])
    # word_service.delete(words[-2])
    input()