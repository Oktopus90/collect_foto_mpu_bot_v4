import os
from uuid import uuid4

from dotenv import load_dotenv
from sqlalchemy import Column, String, create_engine
from sqlalchemy.dialects.postgresql import UUID as pg_UUID  # noqa
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker

load_dotenv()

DATABASE_URL = os.environ['DATABASE_URL']


class PreBase:
    """Класс PreBase является базовым классом для всех моделей в приложении.

    Атрибуты:
    - __tablename__: имя таблицы в базе данных, которое формируется из имени
    класса в нижнем регистре с добавлением 's'.
    - unique_id: уникальный идентификатор модели, который генерируется
    автоматически при создании экземпляра модели.

    Методы:
    - __tablename__: возвращает имя таблицы в базе данных.
    """

    @declared_attr
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'

    unique_id = Column(String, primary_key=True, default=str(uuid4()))


Base = declarative_base(cls=PreBase)

engine = create_engine(DATABASE_URL)

session = sessionmaker(autoflush=False, bind=engine)
