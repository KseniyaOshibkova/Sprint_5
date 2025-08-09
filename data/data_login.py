from enum import Enum


class DataForLoginTests(Enum):
    # Данные для тестов авторизации
    PASSWORD = '123456789'
    REPEAT_LOGIN = 'repeat@mail.com'
    NO_MASK_LOGIN = 'no_mask.com'
    USER = 'User.'
    RED_COLOR = 'FF6972'
    ERROR = 'Ошибка'