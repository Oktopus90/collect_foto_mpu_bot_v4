from .base import AbstractModelForTime


class KontrolPoint(AbstractModelForTime):
    """Модель контрольной точки.

    Модель содержит:
    - number: Номер
    - adres: Адрес
    - coord: Координаты
    - discription: Описание
    - question: Предварительный вопрос
    - comments: Общий коментарий
    - photo: Фотография
    - district: Район
    """
    