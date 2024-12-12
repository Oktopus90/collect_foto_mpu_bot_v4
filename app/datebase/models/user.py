from sqlalchemy import BigInteger, Column, String
from sqlalchemy.dialects.postgresql import UUID as pg_UUID  # noqa

from models.base import AbstractModelForTime


class User(AbstractModelForTime):
    """Модель пользователей телеграма.

    Модель содержит:
    - username: Псевдоним пользователя;
    - name: Имя пользователя;
    - last_name: Фамилия пользователя;
    - telegram_id: ID телеграма пользователя;
    - created_at: Дата и время создания;
    - edited_at: Дата и время редактирования.
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

    def __repr__(self) -> str:
        return (
            f'{self.username=}; {self.role_id=}; '
            f'{self.first_name=}; {self.last_name=}; '
            f'{self.email_id=}; {self.is_active=}; '
            f'{super().__repr__()}'
        )
