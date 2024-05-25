from services.user import user_service
from services.user import UserAlreadyExistsException


def render_signup_page():
    while True:
        print("회원가입을 진행합니다.")
        print("사용할 계정의 사용자명을 입력해주세요 : ", end="")
        username = input()
        print("사용할 계정의 비밀번호를 입력해주세요 : ", end="")
        password = input()
        try:
            user_service.signup(username, password)
            break
        except UserAlreadyExistsException:
            print("존재하는 사용자 이름입니다. 다른 이름을 입력해주세요.")
            continue

    print("회원가입이 완료되었습니다.")
    print("로그인 페이지로 이동합니다.")
