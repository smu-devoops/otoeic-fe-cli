from services.user import UserAlreadyExistsException, user_service
from services.word import Word, word_service

# user마다 자신이 추가한 데이터 + 공용 데이터(관리자가 추가)만 확인가능


def render_word_manage_page():
    print("단어 관리를 시작합니다.")
    # words = word_service.list()

    print("알파벳 오름차순 : 1")
    print("알파벳 내림차순 : 2")
    print("수정시각 오름차순 : 3")
    print("수정시각 내림차순 : 4")

    sort_num = input("정렬 기준을 선택해주세요 : ")
    if sort_num.isdigit() and 1 <= int(sort_num) <= 4:
        sort_num = int(sort_num)
        words = word_service.ordered_list(sort_num)
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        render_word_manage_page()
        return

    # 열 너비 설정
    col_widths = {
        "type": 10,
        "english": 15,
        "korean": 10,
        "level": 10,
        "date_modified": 20,
    }

    # 포맷 문자열 생성
    header_format = f"{{:<{col_widths['type']}}} | {{:<{col_widths['english']}}} | {{:<{col_widths['korean']}}} | {{:<{col_widths['level']}}} | {{:<{col_widths['date_modified']}}}"
    row_format = f"{{:<{col_widths['type']}}} | {{:<{col_widths['english']}}} | {{:<{col_widths['korean']}}} | {{:<{col_widths['level']}}} | {{:<{col_widths['date_modified']}}}"

    # 헤더 출력
    print(
        header_format.format(
            "품사", "영어 철자", "한글 뜻", "난이도", "마지막 수정시각"
        )
    )

    # 데이터 출력
    for word in words:
        print(
            row_format.format(
                word.type, word.english, word.korean, word.level, word.date_modified
            )
        )

    operation_num = int(
        input(
            "단어를 추가하려면 1, 단어를 수정하려면 2, 삭제하려면 3, 단어 관리를 취소하려면 1,2,3을 제외하고 입력하세요. : "
        )
    )
    if operation_num == 1:
        add_word = Word(
            id=None,
            english=input("영어단어를 입력해주세요 : "),
            korean=input("한글단어를 입력해주세요 : "),
            type=input("품사를 입력해주세요 : "),
            level=input("난이도를 입력해주세요 : "),
            date_modified=None,
            date_created=None,
            user_created=1,
        )
        complete_add_word = word_service.create(add_word)

        print(
            "다음과 같이 추가되었습니다 : "
            + complete_add_word.english
            + " "
            + complete_add_word.korean
            + " "
            + complete_add_word.type
            + " "
            + str(complete_add_word.level)
            + " "
        )

    elif operation_num == 2:
        update_word = input("수정하고 싶은 영어단어를 입력해주세요 : ")
        for word in words:
            if word.english == update_word:
                # word.english = input("수정할 영어단어를 입력해주세요 : ")
                word.korean = input("수정할 한글단어를 입력해주세요 : ")
                word.type = input("수정할 품사를 입력해주세요 : ")
                word.level = input("수정할 난이도를 입력해주세요 : ")
                word_service.update(word)
                update_id = word.id
                print(
                    "다음과 같이 수정되었습니다 : "
                    + word_service.get(update_id).english
                    + " "
                    + word_service.get(update_id).korean
                    + " "
                    + word_service.get(update_id).type
                    + " "
                    + str(word_service.get(update_id).level)
                    + " "
                )
                break
        else:
            print("수정하고 싶은 단어가 단어장에 존재하지 않습니다.")

    elif operation_num == 3:
        delete_word = input("삭제하고 싶은 영어단어를 입력해주세요 : ")
        for word in words:
            if word.english == delete_word:
                delete_word_cache = word
                word_service.delete(word)
                print(
                    "다음 단어는 삭제되었습니다 : "
                    + delete_word_cache.english
                    + " "
                    + delete_word_cache.korean
                    + " "
                    + delete_word_cache.type
                    + " "
                    + str(delete_word_cache.level)
                )
                break
        else:
            print("삭제하고 싶은 단어가 단어장에 존재하지 않습니다.")
    else:
        print("단어 관리를 취소합니다.")
