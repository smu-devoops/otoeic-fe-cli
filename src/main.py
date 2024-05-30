from pages.home import render_home_page
from pages.login import render_login_page
from services.user import user_service


def main():
    # TODO
    while True:
        if not user_service.is_logged_in():
            render_login_page()
        else:
            render_home_page()


if __name__ == "__main__":
    main()
