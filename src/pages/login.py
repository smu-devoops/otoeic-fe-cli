from services.user import user_service

from pages.signup import render_signup_page


def render_login_page():
    # TODO
    # 만약 사용자가 회원가입을 원한다면...
    user = user_service.login("이찬민", "이찬민")
    print(user)

    # render_signup_page()
    pass
