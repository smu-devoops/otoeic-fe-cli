from app.pages import get_initial_page


class Application:
    def run(self):
        page = get_initial_page()
        while page is not None:
            page = page.visit()
