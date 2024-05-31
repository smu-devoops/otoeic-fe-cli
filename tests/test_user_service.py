import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from unittest.mock import patch, MagicMock
from services.user import UserService, User, UserAlreadyExistsException, UserInfoEmptyException, UserNotFoundException

@pytest.fixture
def mock_requests():
    # requests 모듈을 모의(mock)하여 실제 HTTP 요청이 발생하지 않도록 합니다.
    with patch('services.user.requests') as mock:
        yield mock

@pytest.fixture
def user_service():
    # UserService 인스턴스를 생성합니다.
    return UserService()

def test_login_success(mock_requests, user_service):
    # 성공적인 로그인 시나리오를 테스트합니다.
    # requests.get 호출에 대한 응답을 모의하여 올바른 사용자 정보를 반환합니다.
    mock_response = MagicMock()
    mock_response.json.return_value = [
        {'id': 1, 'username': 'test_user', 'password': 'test_password', 'level': 1, 'is_admin': False, 'streak': 0, 'streak_freeze_amount': 0, 'is_streak_freeze_activated': False, 'point': 0}
    ]
    mock_requests.get.return_value = mock_response

    # UserService의 login 메서드를 호출합니다.
    user = user_service.login('test_user', 'test_password')
    
    # 반환된 사용자가 None이 아니고, username이 'test_user'인지 확인합니다.
    assert user is not None
    assert user.username == 'test_user'
    
    # 현재 사용자가 로그인된 사용자와 같은지 확인합니다.
    assert user_service.current_user() == user

def test_login_failure(mock_requests, user_service):
    # 실패한 로그인 시나리오를 테스트합니다.
    # requests.get 호출에 대한 응답을 모의하여 빈 사용자 목록을 반환합니다.
    mock_response = MagicMock()
    mock_response.json.return_value = []
    mock_requests.get.return_value = mock_response

    # UserService의 login 메서드를 예외 검사
    with pytest.raises(UserInfoEmptyException):
        user_service.login('', 'password')  # 빈 사용자 이름으로 예외 발생 확인
    with pytest.raises(UserInfoEmptyException):
        user_service.login('username', '')  # 빈 사용자 이름으로 예외 발생 확인

    with pytest.raises(UserNotFoundException):
        user_service.login('wrong_user', 'wrong_password')  # DB에 없는 정보로 로그인할 때

def test_logout(user_service):
    # 로그아웃 기능을 테스트합니다.
    # 현재 사용자 정보를 설정합니다.
    user_service._current_user = User({
        'id': 1, 'username': 'test_user', 'level': 1, 'is_admin': False, 'streak': 0, 'streak_freeze_amount': 0, 'is_streak_freeze_activated': False, 'point': 0
    })
    
    # UserService의 logout 메서드를 호출합니다.
    user_service.logout()
    
    # 현재 사용자가 None인지 확인합니다.
    assert user_service.current_user() is None

def test_signup_success(mock_requests, user_service):
    # 성공적인 회원가입 시나리오를 테스트합니다.
    # requests.post 호출에 대한 응답을 모의하여 상태 코드 201을 반환합니다.
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_requests.post.return_value = mock_response

    # UserService의 signup 메서드를 호출합니다.
    user_service.signup('new_user', 'new_password')

    # requests.post가 호출되었는지 확인합니다.
    assert mock_requests.post.called

def test_signup_failure(mock_requests, user_service):
    # 실패한 회원가입 시나리오를 테스트합니다.
    # requests.post 호출에 대한 응답을 모의하여 상태 코드 400을 반환합니다.
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_requests.post.return_value = mock_response

    # UserService의 signup 메서드를 호출하여 UserAlreadyExistsException이 발생하는지 확인합니다.
    with pytest.raises(UserInfoEmptyException):
        user_service.signup('', 'password')  # 빈 사용자 이름으로 예외 발생 확인
    with pytest.raises(UserInfoEmptyException):
        user_service.signup('username', '')  # 빈 사용자 이름으로 예외 발생 확인
