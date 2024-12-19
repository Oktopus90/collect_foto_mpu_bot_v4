from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import AbstractModelForTime


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
    - author: Автор КП
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
    author = relationship(
        "User",
        back_populates='kontrol_points',
    )
    author_id = Column(
        String,
        ForeignKey("users.unique_id"),
    )

    def __repr__(self) -> str:
        return (
            f'{self.number=};'
            f'{self.discription=}; {self.question=}; '
            f'{super().__repr__()}'
        )
