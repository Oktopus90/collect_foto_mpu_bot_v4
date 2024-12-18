from sqlalchemy import BigInteger, Column, String
from sqlalchemy.dialects.postgresql import UUID as pg_UUID  # noqa
from sqlalchemy.orm import relationship

from .base import AbstractModelForTime


class User(AbstractModelForTime):
    """Модель пользователей телеграма.

    Модель содержит:
    - username: Псевдоним пользователя;
    - name: Имя пользователя;
    - last_name: Фамилия пользователя;
    - telegram_id: ID телеграма пользователя;
    - created_at: Дата и время создания;
    - edited_at: Дата и время редактирования;
    - kontrol_points: Ссылка на КП от данного автора.
    """

    username = Column(
        String(length=255),
        unique=True,
    )
    first_name = Column(
        String(length=255),
        nullable=True,
    )
    last_name = Column(
        String(length=255),
        nullable=True,
    )
    telegram_id: Column[int] = Column(
        BigInteger,
        unique=True,
    )
    kontrol_points = relationship(
        "KontrolPoint",
        back_populates="author",
    )

    def __repr__(self) -> str:
        return (
            f'{self.username=};'
            f'{self.first_name=}; {self.last_name=}; '
            f'{super().__repr__()}'
        )
