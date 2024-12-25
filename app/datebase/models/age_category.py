from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import AbstractModelForTime


class AgeCategory(AbstractModelForTime):
    """Модель района.

    Модель содержит:
    - name: Название возрастной категории (1-2, 3-4 ...)
    - color: цветовое обозначение категории
    - kontrol_points: Ссылка на КП в этом районе.
    """

    name = Column(
        String(length=255),
    )
    color = Column(
        String(length=255),
    )

    def __repr__(self) -> str:
        return (
            f'{self.name=};'
        )
