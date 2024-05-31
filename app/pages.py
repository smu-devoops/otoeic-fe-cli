from __future__ import annotations

from app.apis import api_client


class Page:
    def render(self) -> Page | None:
        """페이지를 렌더링하고 다음 페이지를 반환한다."""
        raise NotImplementedError


class MenuPage(Page):
    # TODO: @김동주 - 메뉴 페이지를 구현해주세요.
    def render(self) -> Page | None:
        self._print_welcome_message()
        selected_menu = self._select_menu()
        if selected_menu == 1:
            return LoginPage()
        if selected_menu == 2:
            return SignupPage()
        if selected_menu == 3:
            return None # 종료

    def _select_menu(self) -> int:
        while True:
            self._print_menu()
            input_num = input()
            if input_num.isdigit() == False:
                print("숫자로 입력해주세요.")
                continue
            if int(input_num) not in [1, 2, 3]:
                print("메뉴 범위를 벗어났습니다. 다시 입력해주세요.")
                continue
            break
        return int(input_num)

    def _print_welcome_message(self) -> None:
        print("오토익 영어 단어 학습장에 오신 것을 환영합니다! ")

    def _print_menu(self) -> None:
        print("로그인하시려면 1, 회원가입하시려면 2, 프로그램 종료를 원하면 3을 입력하세요.")


class LoginPage(Page):
    # TODO: @이찬민 - 로그인 페이지를 구현해주세요.
    pass


class SignupPage(Page):
    # TODO: @이찬민 - 회원가입 페이지를 구현해주세요.
    pass


class UserHomePage(Page):
    # TODO
    pass
