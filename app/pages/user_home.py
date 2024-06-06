from app.pages.base import Page


class UserHomePage(Page):
    def visit(self):
        print(
            "-------------------------사용자 홈 페이지입니다---------------------------------"
        )
        menu_num = input(
            "일반 단어 테스트는 1, 내 수준 점검하기는 2, 단어 관리는 3, 로그아웃을 원하면 4를 입력하세요. "
        )
        if menu_num not in [1, 2, 3, 4]:
            print("메뉴 숫자가 아닙니다.")
            return UserHomePage()
        if menu_num == "1":
            print("일반 단어 테스트 페이지로 이동합니다.")
            return WordTestPage()
        if menu_num == "2":
            print("내 수준 점검하기 페이지로 이동합니다.")
            return WordLevelTestPage()
        if menu_num == "3":
            print("단어 관리 페이지로 이동합니다.")
            return WordManagePage()
        if menu_num == "4":
            print("로그인 메뉴 페이지로 이동합니다.")
            return MenuPage()


"""
visit() 에서 사용할 페이지를 이곳에 import 해주세요.
"""
from app.pages.menu import MenuPage
from app.pages.word_manage import WordManagePage
from app.pages.word_test import WordTestPage
from app.pages.word_level_test import WordLevelTestPage
