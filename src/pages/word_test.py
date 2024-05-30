import datetime
import random

from pages.signup import render_signup_page
from services.exam import Exam, Question, exam_service
from services.user import User, user_service
from services.word import Word, word_service


def render_word_test_page(type):
    normal_test_level = 0
    normal_test_amount = 0
    if type == "normal":
        normal_test_level = input(
            "시험 난이도를 선택하세요 (1,2,3,4 중 하나를 입력하세요): "
        )
        if normal_test_amount.isdigit() and 1 <= int(normal_test_amount) <= 4:
            normal_test_amount = int(normal_test_amount)
            normal_test_amount = int(input("시험 문제 개수를 선택하세요 : "))
            my_exam = Exam(
                id=None,
                level=normal_test_level,
                amount=normal_test_amount,
                ranked=False,
                date_created=None,
                date_submitted=None,
                questions=None,
            )
        else:
            print("잘못 입력하셨습니다. 다시 시도해주세요.")
            render_word_test_page(type)
            return

    elif type == "levelcheck":
        options = [1, 2, 3, 4]
        selected = random.choice(options)
        normal_test_level = selected
        normal_test_amount = 10
        my_exam = Exam(
            id=None,
            level=normal_test_level,
            amount=normal_test_amount,
            ranked=True,
            date_created=None,
            date_submitted=None,
            questions=None,
        )

    my_exam = exam_service.get_exam(my_exam)
    question_list = exam_service.get_question_list(
        my_exam
    )  # questionWord(korean, type) 배열로 옴

    print("단어 테스트를 시작합니다.")
    print("⭐ 왼쪽의 뜻에 맞는 영어단어를 입력하세요. ⭐")
    print(" * 단어 테스트를 중단하려면 0를 입력하세요")
    count = 0
    answer_list = []
    for question in question_list:
        count += 1
        answer = input(
            str(count)
            + "."
            + "("
            # + question.word["type"]
            + question.word.type
            + ")"
            + question.word.korean
            + ": "
        )
        answer_list.append(answer)  # str타입 배열
    print(answer_list)
    exam_service.submit(my_exam, answer_list)
    print("단어 테스트를 종료합니다.")
    return
