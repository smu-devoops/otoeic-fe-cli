from app.apis import api
from app.pages.base import Page


class SignupPage(Page):
    def render(self):
        print(
            "-------------------------회원가입 페이지입니다---------------------------------"
        )
        username = input("사용자명을 입력해주세요:")
        password = input("비밀번호를 입력해주세요:")

        # signup post
        user = api.user.register(username, password)
        # 회원가입 성공시 LoginPage로 이동
        if user is not None:
            print("회원가입 성공!", user)
            return LoginPage()
        # 회원가입 실패시 다시 회원가입 페이지로 이동
        else:
            return SignupPage()


"""
render() 에서 사용할 페이지를 이곳에 import 해주세요.
"""
from app.pages.login import LoginPage
