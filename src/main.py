from services.user import user_service

from pages.login import render_login_page
from pages.home import render_home_page


def main():
    # TODO
    while True:
        if user_service.current_user() == None:
            render_login_page()
        else:
            render_home_page()


if __name__ == "__main__":
    main()
