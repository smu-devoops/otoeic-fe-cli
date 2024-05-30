from pages.signup import render_signup_page
from services.user import User, UserInfoEmptyException, user_service
from services.word import Word, word_service


def render_login_page():
    print("\n오토익 영어 단어 학습장에 오신 것을 환영합니다! ")
    print("로그인하시려면 1, 회원가입하시려면 2를 입력하세요.")
    input_num = int(input())
    if input_num == 2:
        render_signup_page()
        return

    print("사용자명을 입력해주세요 : ", end="")
    username = input()
    print("비밀번호를 입력해주세요 : ", end="")
    password = input()

    user = user_service.login(username=username, password=password)
    # 예외처리
    try:
        result = user_service.login(username, password)
    except UserInfoEmptyException as e:
        print(e)

    if user_service.current_user():
        print("로그인에 성공하였습니다! 사용자 홈 화면으로 이동합니다.")
    else:
        print("로그인에 실패하였습니다.")
