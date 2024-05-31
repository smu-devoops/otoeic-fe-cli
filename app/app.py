from __future__ import annotations

from . import pages


class Application:
    def __init__(self) -> None:
        page = pages.MenuPage()
        self._start(page)

    def _start(self, page: pages.Page):
        while page is not None:
            page = page.render()
