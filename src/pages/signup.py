from services.user import (
    UserAlreadyExistsException,
    UserInfoEmptyException,
    user_service,
)


def render_signup_page():
    while True:
        print("회원가입을 진행합니다. 진행 중 취소를 원하시면 q를 눌러주세요")
        print("사용할 계정의 사용자명을 입력해주세요 : ", end="")
        username = input()
        if username == "q":
            print("회원가입이 취소되었습니다.")
            print("로그인 페이지로 이동합니다.")
            return
        print("사용할 계정의 비밀번호를 입력해주세요 : ", end="")
        password = input()
        if password == "q":
            print("회원가입이 취소되었습니다.")
            print("로그인 페이지로 이동합니다.")
            return

        # 예외처리
        try:
            result = user_service.signup(username, password)
            if result:
                print("회원 가입이 완료되었습니다. 로그인 화면으로 이동합니다.")
        except UserAlreadyExistsException as e:
            print(e)
        except UserInfoEmptyException as e:
            print(e)

    print("회원가입이 완료되었습니다.")
    print("로그인 페이지로 이동합니다.")
