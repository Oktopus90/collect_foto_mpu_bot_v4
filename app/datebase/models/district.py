from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import AbstractModelForTime


class District(AbstractModelForTime):
    """Модель района.

    Модель содержит:
    - name: Название района
    - kontrol_points: Ссылка на КП в этом районе.
    """

    username = Column(
        String(length=255),
    )
    kontrol_points = relationship(
        "KontrolPoint",
        back_populates="district",
    )

    def __repr__(self) -> str:
        return (
            f'{self.username=};'
        )
