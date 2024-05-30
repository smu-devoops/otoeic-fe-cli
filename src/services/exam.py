from __future__ import annotations

import dataclasses
import datetime
import random
import typing

import requests
from constants import HOST
from services.user import User
from services.word import Word


class WordAlreadyExistsException(Exception):
    pass


@dataclasses.dataclass
class Question:
    word: QuestionWord
    order: int
    # submitted_answer: str


@dataclasses.dataclass
class QuestionWord:
    korean: str
    type: str


@dataclasses.dataclass
class Exam:
    id: int
    # user: User
    level: int
    amount: int
    ranked: bool
    # point: int
    # user_created:
    date_created: datetime.datetime
    date_submitted: datetime.datetime
    questions: typing.List[Question]


class ExamService:
    # API 요청으로 exam 클래스 객체 받아오는 메소드
    def get_exam(self, exam: Exam) -> Exam:
        exam_data = requests.post(
            HOST + "/exam",
            data={"level": exam.level, "amount": exam.amount, "ranked": exam.ranked},
        )
        exam_data = exam_data.json()
        # res_exam = Exam(**exam_data)
        res_exam = Exam(
            id=exam_data["id"],
            level=exam_data["level"],
            amount=exam_data["amount"],
            ranked=exam_data["ranked"],
            date_created=exam_data["date_created"],
            date_submitted=exam_data["date_submitted"],
            questions=exam_data["questions"],
        )
        return res_exam

    def get_question_list(self, exam: Exam) -> typing.List[Question]:
        question_list = []
        for question in exam.questions:
            word_data = question["word"]
            word = QuestionWord(
                korean=word_data["korean"],
                type=word_data["type"],
            )
            # question_dic = QuestionWord(**word)
            question_list.append(word)
            # question_dic = Question(word=word, order=question.order, submitted_answer=question.submitted_answer)
            # question_list.append(question_dic)

        return question_list

    # 받아온 exam 클래스 객체를 화면에 출력해주는 메소드
    def print_exam(self, exam: Exam) -> None:
        for question in exam.questions:
            print(question.word.korean)
            print(question.word.type)

    # 사용자 문제를 푼 answer_list를 받아서 exam/id/submit로 post
    def submit(self, exam: Exam, answer_list: typing.List[str]) -> None:

        print(HOST + "/exam/" + str(exam.id) + "/submit")
        exam_data = requests.post(
            HOST + "/exam/" + str(exam.id) + "/submit", data={"answers": answer_list}
        )
        # exam_data = exam_data.json()
        return


exam_service = ExamService()
