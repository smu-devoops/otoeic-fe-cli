from services.user import user_service

from .word_manage import render_word_manage_page
from .word_test import render_word_test_page


def render_home_page():
    my_user = user_service.current_user()
    print("\n" + my_user.username + "님의 사용자 홈입니다.")
    print(my_user.username + "님의 단어 레벨은 [" + str(my_user.level) + "] 입니다.")

    print("다음에 해당하는 명령으로 메뉴를 실행하세요!")
    print("일반 단어 테스트 : 1")
    print("내 수준 점검하기 : 2")
    print("단어 관리하기 : 3")

    menu_input = input()
    if str(0) <= menu_input <= str(9):
        menu_num = int(menu_input)
        if menu_num == 1:
            render_word_test_page("normal")
        elif menu_num == 2:
            render_word_test_page("levelcheck")
        elif menu_num == 3:
            render_word_manage_page()
        else:
            print("잘못된 명령입니다.")
    else:
        print("한 자리 숫자가 아닙니다.")
