from app.apis import api
from app.pages.base import Page


class LoginPage(Page):

    def render(self):
        print(
            "-------------------------로그인 페이지입니다---------------------------------"
        )
        username = input("사용자명을 입력해주세요:")
        password = input("비밀번호를 입력해주세요:")

        # login post
        user = api.user.login(username, password)

        # 로그인 성공시 UserHomePage로 이동
        if user is not None:
            print("로그인 성공!", user)
            return UserHomePage()
        # 로그인 실패시 다시 로그인 페이지로 이동
        else:
            return LoginPage()


"""
render() 에서 사용할 페이지를 이곳에 import 해주세요.
"""
from app.pages.user_home import UserHomePage
