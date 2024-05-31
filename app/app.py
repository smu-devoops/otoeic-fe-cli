from __future__ import annotations

from app.pages import Page
from app.pages import MenuPage


class Application:
    def __init__(self) -> None:
        page = MenuPage()
        self._start(page)

    def _start(self, page: Page):
        while page is not None:
            page = page.render()
