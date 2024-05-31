from __future__ import annotations


class Page:
    def render(self) -> Page | None:
        """페이지를 렌더링하고 다음 페이지를 반환한다."""
        raise NotImplementedError


class MenuPage(Page):
    # TODO: @김동주 - 메뉴 페이지를 구현해주세요.
    pass

class LoginPage(Page):
    # TODO: @이찬민 - 로그인 페이지를 구현해주세요.
    pass


class SignupPage(Page):
    # TODO: @이찬민 - 회원가입 페이지를 구현해주세요.
    pass


class UserHomePage(Page):
    # TODO
    pass
