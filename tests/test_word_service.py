import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import datetime
from unittest.mock import MagicMock, patch

import pytest
from services.word import (
    Word,
    WordAlreadyExistsException,
    WordDataBaseFullException,
    WordInfoEmptyException,
    WordNotFoundException,
    WordService,
)

# 테스트 데이터 생성
mock_word_list = [
    Word(
        id=1,
        english="test",
        korean="테스트",
        type="noun",
        level=1,
        date_modified=datetime.datetime.now(),
        date_created=datetime.datetime.now(),
        user_created=1,
    ),
    Word(
        id=2,
        english="socket",
        korean="소켓",
        type="noun",
        level=1,
        date_modified=datetime.datetime.now(),
        date_created=datetime.datetime.now(),
        user_created=1,
    ),
    Word(
        id=3,
        english="police",
        korean="경찰",
        type="noun",
        level=1,
        date_modified=datetime.datetime.now(),
        date_created=datetime.datetime.now(),
        user_created=1,
    ),
]


@pytest.fixture
def mock_requests():
    # requests 모듈을 모의(mock)하여 실제 HTTP 요청이 발생하지 않도록 합니다.
    with patch("services.word.requests") as mock:
        yield mock


# fixture 데코레이터로 word_service 객체를 test용으로 만들어 줌 ( list 반환이 mock 데이터로 고정됨 )
@pytest.fixture
def word_service():
    word_service = WordService()
    # WordService의 list 메서드를 모의하여 mock_word_list를 반환합니다.
    with patch.object(WordService, "list", return_value=mock_word_list):
        yield word_service


def test_create_word_success(mock_requests, word_service):
    # 성공적인 단어 생성 시나리오를 테스트합니다.
    # requests.post 호출에 대한 응답을 모의하여 상태 코드 201을 반환합니다.
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_requests.post.return_value = mock_response

    # 테스트에 사용할 단어 객체를 생성합니다.
    word = Word(
        id=4,
        english="cat",
        korean="고양이",
        type="noun",
        level=1,
        date_modified=datetime.datetime.now(),
        date_created=datetime.datetime.now(),
        user_created=1,
    )

    # WordService의 create 메서드를 호출합니다.
    response = word_service.create(word)

    # 응답 상태 코드가 201인지 확인합니다.
    assert response.status_code == 201

    # requests.post가 호출되었는지 확인합니다.
    assert mock_requests.post.called


def test_create_word_failure(mock_requests, word_service):
    # 실패한 단어 생성 시나리오를 테스트합니다.
    # requests.post 호출에 대한 응답을 모의하여 상태 코드 400을 반환합니다.
    mock_response_post = MagicMock()
    mock_response_post.status_code = 400
    mock_requests.post.return_value = mock_response_post

    # 테스트에 사용할 단어 객체를 생성합니다.
    word_dup = mock_word_list[1]
    word_wrong_korean = Word(
        id=4,
        english="cat",
        korean="",
        type="noun",
        level=1,
        date_modified=datetime.datetime.now(),
        date_created=datetime.datetime.now(),
        user_created=1,
    )

    with pytest.raises(WordAlreadyExistsException):
        word_service.create(word_dup)
    with pytest.raises(WordInfoEmptyException):
        word_service.create(word_wrong_korean)


def test_get_word(mock_requests, word_service):
    # 특정 단어를 가져오는 시나리오를 테스트합니다.
    # requests.get 호출에 대한 응답을 모의하여 단일 단어 정보를 반환합니다.
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {
            "id": 1,
            "english": "test",
            "korean": "테스트",
            "type": "noun",
            "level": 1,
            "date_modified": str(datetime.datetime.now()),
            "date_created": str(datetime.datetime.now()),
            "user_created": 1,
        }
    ]
    mock_requests.get.return_value = mock_response

    # WordService의 get 메서드를 호출합니다.
    word = word_service.get(1)

    # 반환된 단어 객체가 None이 아닌지 확인합니다.
    assert word is not None

    # 단어의 영어 단어가 "test"인지 확인합니다.
    assert word.english == "test"


def test_list_words(mock_requests, word_service):
    # 모든 단어를 가져오는 시나리오를 테스트합니다.
    # requests.get 호출에 대한 응답을 모의하여 단어 목록을 반환합니다.
    # mock_response = MagicMock()

    # WordService의 list 메서드를 호출합니다.
    words = word_service.list()

    # 반환된 단어 목록의 길이가 2인지 확인합니다.
    assert len(words) == 3

    # 첫 번째 단어의 영어 단어가 "test1"인지 확인합니다.
    assert words[0].english == "test"


def test_ordered_list_words(mock_requests, word_service):
    # 정렬된 단어 목록을 가져오는 시나리오를 테스트합니다.
    # requests.get 호출에 대한 응답을 모의하여 정렬된 단어 목록을 반환합니다.
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {
            "id": 1,
            "english": "apple",
            "korean": "사과",
            "type": "noun",
            "level": 1,
            "date_modified": str(datetime.datetime.now()),
            "date_created": str(datetime.datetime.now()),
            "user_created": 1,
        },
        {
            "id": 2,
            "english": "banana",
            "korean": "바나나",
            "type": "noun",
            "level": 1,
            "date_modified": str(datetime.datetime.now()),
            "date_created": str(datetime.datetime.now()),
            "user_created": 1,
        },
    ]
    mock_requests.get.return_value = mock_response

    # WordService의 ordered_list 메서드를 호출합니다.
    words = word_service.ordered_list(3)

    # 반환된 단어 목록의 길이가 2인지 확인합니다.
    assert len(words) == 2

    # 첫 번째 단어의 영어 단어가 "apple"인지 확인합니다.
    assert words[0].english == "apple"


def test_update_word_success(mock_requests, word_service):
    # 성공적인 단어 업데이트 시나리오를 테스트합니다.
    # requests.patch 호출에 대한 응답을 모의하여 상태 코드 200을 반환합니다.
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_requests.patch.return_value = mock_response

    # 테스트에 사용할 단어 객체를 생성합니다.
    word = Word(
        id=5,
        english="success",
        korean="성공",
        type="noun",
        level=1,
        date_modified=datetime.datetime.now(),
        date_created=datetime.datetime.now(),
        user_created=1,
    )

    # WordService의 update 메서드를 호출합니다.
    word_service.update(word)

    # requests.patch가 호출되었는지 확인합니다.
    assert mock_requests.patch.called


def test_delete_word_success(mock_requests, word_service):
    # 성공적인 단어 삭제 시나리오를 테스트합니다.
    # requests.delete 호출에 대한 응답을 모의하여 상태 코드 200을 반환합니다.
    mock_response = MagicMock()

    # 테스트에 사용할 단어 객체를 생성합니다.
    word = mock_word_list[0]
    print(word.id)


def test_delete_word_failure(mock_requests, word_service):
    mock_response = MagicMock()
    mock_requests.delete.return_value = mock_response

    word = Word(
        id=5,
        english="failure",
        korean="실패",
        type="noun",
        level=1,
        date_modified=datetime.datetime.now(),
        date_created=datetime.datetime.now(),
        user_created=1,
    )

    with pytest.raises(WordNotFoundException):
        word_service.delete(word)
