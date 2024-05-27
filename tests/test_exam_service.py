import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from unittest.mock import patch, MagicMock
from services.exam import ExamService, Exam, Question
from services.user import User
from services.word import Word
import datetime
from constants import HOST

@pytest.fixture
def mock_requests():
    with patch('services.exam.requests') as mock:
        yield mock

@pytest.fixture
def exam_service():
    return ExamService()

@pytest.fixture
def sample_exam():
    user_data = {
        'id': 1,
        'username': 'test_user',
        'level': 1,
        'is_admin': False,
        'streak': 0,
        'streak_freeze_amount': 0,
        'is_streak_freeze_activated': False,
        'point': 0
    }
    user = User(user_data)
    
    word = Word(
        id=1,
        english='test',
        korean='테스트',
        type='noun',
        level=1,
        date_modified=None,
        date_created=None,
        user_created=1
    )
    question = Question(word=word, order=1, submitted_answer='')
    exam = Exam(
        id=1,
        user=user,
        level=1,
        amount=1,
        point=0,
        date_created=datetime.datetime.now(),
        date_submitted=datetime.datetime.now(),
        questions=[question]
    )
    return exam

def test_get_exam(mock_requests, exam_service, sample_exam):
    # Mock the response from the requests.post call
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "id": 1,
        "user": {
            "id": 1,
            "username": "test_user",
            "level": 1,
            "is_admin": False,
            "streak": 0,
            "streak_freeze_amount": 0,
            "is_streak_freeze_activated": False,
            "point": 0
        },
        "level": 1,
        "amount": 1,
        "point": 0,
        "date_created": str(datetime.datetime.now()),
        "date_submitted": str(datetime.datetime.now()),
        "questions": [
            {
                "word": {
                    "id": 1,
                    "english": "test",
                    "korean": "테스트",
                    "type": "noun",
                    "level": 1,
                    "date_modified": str(datetime.datetime.now()),
                    "date_created": str(datetime.datetime.now()),
                    "user_created": 1
                },
                "order": 1,
                "submitted_answer": ""
            }
        ]
    }
    mock_requests.post.return_value = mock_response

    exam = exam_service.get_exam(sample_exam)
    assert exam.id == 1
    assert exam.user.username == 'test_user'
    assert len(exam.questions) == 1

def test_get_question_list(mock_requests, exam_service, sample_exam):
    question_list = exam_service.get_question_list(sample_exam)
    assert len(question_list) == 1
    assert question_list[0].word.english == 'test'

def test_submit_exam(mock_requests, exam_service, sample_exam):
    # Mock the response from the requests.post call
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.post.return_value = mock_response

    answer_list = ['test_answer']
    exam_service.submit(sample_exam, answer_list)
    assert mock_requests.post.called
    mock_requests.post.assert_called_with(f'{HOST}/exam/1/submit', data={'answers': answer_list})
