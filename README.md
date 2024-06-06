# OTOEIC Front-End (Command Line Interface ver.)

## Class Diagram


```mermaid
classDiagram
direction TB


class Application
Application : +run() None
Application ..> Page


class Page
<<interface>> Page
Page : +visit() Optional[Page]
Page <|.. MenuPage
Page <|.. LoginPage
Page <|.. SignupPage
Page <|.. UserHomePage
Page <|.. WordManagePage
Page <|.. WordTestPage
Page <|.. WordLevelTestPage
note for Page "class Application:
&nbsp;&nbsp;&nbsp;&nbsp;...
&nbsp;&nbsp;&nbsp;&nbsp;def run(self):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;page = get_initial_page()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;while page is not None:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;page = page.visit()

Application.run()은 Page.visit()이 return으로 전달하는 Page로 이동한다.
만약, 프로그램을 종료하고 싶다면 None 을 반환한다."


LoginPage ..> API

SignupPage ..> API

UserHomePage ..> API

WordManagePage ..> API

WordTestPage ..> API
WordTestPage : -exam ExamDTO

WordLevelTestPage ..> API
WordLevelTestPage : -exam ExamDTO


class UserDTO
<<readonly>> UserDTO
UserDTO : +id int
UserDTO : +username str
UserDTO : +freeze_activated bool
UserDTO : +freeze_amount int
UserDTO : +level int
UserDTO : +point int
UserDTO : +streak int
UserDTO : +date_created datetime
UserDTO : +is_staff bool


class WordDTO
WordDTO : +id Optional[int]
WordDTO : +english str
WordDTO : +korean str
WordDTO : +type str
WordDTO : +level int
WordDTO : +date_modified Optional[datetime]
WordDTO : +date_created Optional[datetime]
WordDTO : +user_created Optional[UserDTO]


class ExamDTO
ExamDTO : +id Optional[int]
ExamDTO : +level int
ExamDTO : +questions int
ExamDTO : +is_ranked bool
ExamDTO : +point Optional[int]
ExamDTO : +date_created Optional[datetime]
ExamDTO : +date_submitted Optional[datetime]


class QuestionDTO
QuestionDTO : +id Optional[int]
QuestionDTO : +eng Optional[str]
QuestionDTO : +kor str
QuestionDTO : +type str
QuestionDTO : +answer Optional[str]
QuestionDTO : +is_correct Optional[bool]
note for QuestionDTO "만약 응시한 시험에 정답을 제출하고자 한다면,
각 QuestionDTO.answer 들을 수정한 뒤, ExamAPI.submit() 에 전달하도록 한다."


class API
API : +user UserAPI
API : +word WordAPI
API : +exam ExamAPI
API ..> UserAPI
API ..> WordAPI
API ..> ExamAPI


class UserAPI
<<interface>> UserAPI
UserAPI : +register(str username, str password) UserDTO
UserAPI : +login(str username, str password) UserDTO
UserAPI : +is_logged_in() bool
UserAPI : +current_user() UserDTO
UserAPI : +update(UserDTO user) UserDTO
UserAPI ..> UserDTO
note for UserAPI "스트릭프리즈를 구매하고 싶다면, UserDTO.freeze_amount 를 조정하여 update()에 전달하면 된다.
스트릭프리즈를 활성화하고 싶다면, UserDTO.freeze_activated 를 조정하여 update()에 전달하면 된다."


class WordAPI
<<interface>> WordAPI
WordAPI : +create(WordDTO word) WordDTO
WordAPI : +list(str sort_by) List~WordDTO~
WordAPI : +update(WordDTO word) WordDTO
WordAPI : +delete(WordDTO word) None
WordAPI ..> WordDTO


class ExamAPI
<<interface>> ExamAPI
ExamAPI : +create(ExamDTO exam) ExamDTO
ExamAPI : +get_questions(ExamDTO exam) Tuple[Question]
ExamAPI : +submit(ExamDTO exam, Tuple[Question] questions) ExamDTO
ExamAPI ..> ExamDTO
ExamAPI ..> QuestionDTO
note for ExamAPI "날짜별 시험(스트릭) 조회를 하려면 ExamAPI.list()로 조회한 시험의 각 날짜를 참고한다."
```