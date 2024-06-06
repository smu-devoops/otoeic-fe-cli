from __future__ import annotations

from app.pages import *


class Application:
    def run(self):
        page = get_initial_page()
        while page is not None:
            page = page.visit()
