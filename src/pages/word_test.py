from services.user import user_service
from services.word import word_service
from services.exam import exam_service


from pages.signup import render_signup_page
from services.user import User
from services.word import Word
from services.exam import Exam
from services.exam import Question

def render_word_test_page(type):
    normal_test_level = 0
    normal_test_amount = 0
    if type == "normal" :
        normal_test_level = int(input("시험 난이도를 선택하세요 : "))
        normal_test_amount = int(input("시험 문제 개수를 선택하세요 : "))
    elif type == "levelcheck" :
        normal_test_level = 2
        normal_test_amount = 10
    
    my_exam = Exam(id=None, user=user_service.current_user().id,level=normal_test_level,amount=normal_test_amount, point=0, date_created=None, date_submitted=None,questions=None )
    my_exam = exam_service.get_exam(my_exam)
    question_list = exam_service.get_question_list(my_exam)

    print("단어 테스트를 시작합니다.")
    print("⭐ 왼쪽의 뜻에 맞는 영어단어를 입력하세요. ⭐")
    count = 0
    answer_list = []
    for question in question_list:
        count += 1
        answer = input(str(count)+"." + "(" + question.word["type"] + ")" + question.word["korean"] + ": ")
        answer_list.append(answer)
    print(answer_list)
    exam_service.submit(my_exam, answer_list)