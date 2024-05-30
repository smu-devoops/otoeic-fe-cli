# from __future__ import annotations

# import dataclasses
# import datetime
# import random
# import typing

# import requests
# from constants import HOST
# from services.user import User, user_service

# # @dataclasses.dataclass
# # class Streak:
# #     user: User
# #     pass


# class UserNotLoginException(Exception):
#     pass


# class StreakService:
#     def read_calendar(self, user: User):
#         res = requests.get(HOST + "/streak/calendar/" + str(user.id))
#         data = res.json()
#         calendar = data["calendar"]
#         return calendar

#     def buy_streak_freeze(self, user: User):
#         if user_service.current_user != user:
#             raise UserNotLoginException
#         res = requests.post(HOST + "/streak/freeze")

#     def toggle_streak_freeze(self):
#         pass


# streak_service = StreakService()
