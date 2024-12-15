from .base import AbstractModelForTime
from sqlalchemy import BigInteger, Column, String, Integer, Float


class KontrolPoint(AbstractModelForTime):
    """Модель контрольной точки.

    Модель содержит:
    - number: Номер
    - adres: Адрес
    - latitude: Широта
    - longitude: Долгота
    - district: Район
    - question: Предварительный вопрос
    - discription: Описание
    - comments: Общий коментарий
    - photo: Фотография
    """

    number = Column(
        Integer,
        unique=True,
        autoincrement=True,
    )
    adres = Column(
        String(length=255),
    )
    latitude = (
        Float()
    )
    longitude = (
        Float()
    )
    district = Column(
        String(length=255),
    )
    question = Column(
        String(length=255),
    )
    discription = Column(
        String(length=255),
    )
    comments = Column(
        String(length=255),
    )
    photo = Column(
        String(length=255),
    )
