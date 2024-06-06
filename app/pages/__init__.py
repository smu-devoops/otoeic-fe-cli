from app.pages.base import Page


def get_initial_page() -> Page:
    from app.pages.menu import MenuPage
    return MenuPage()
