from datebase.core.db import session
from datebase.models.kontrol_point import KontrolPoint
from datebase.models.age_category import AgeCategory
from datebase.models.district import District
from datebase.models.user import User
from utils.logger import get_logger

logger = get_logger(__name__)


def add_kontrol_point(data: dict[str, str]) -> None:
    """Добаление КП в БД.

    Args:
        data (dict): {
            'number': Номер_КП
            'adres': Адрес
            'latitude': широта
            'longitude': Долгота
            'question': Вопрос
            'discription': Описание
            'comments': Коментарий
            'photo': ссылка на папку на ЯДиске
            'age_category': вохрастная категория
            'author': Автор
            'district': Район
        }.

    Returns:
        None.

    """
    with session() as sess:
        kp = KontrolPoint(
            number=int(data['number']),
            adres=data['adres'],
            latitude=float(data['latitude']),
            longitude=float(data['longitude']),
            question=data['question'],
            discription=data['discription'],
            comments=data['comments'],
            photo=str(data['photo']),
            age_category=data['age_category'],
            author=data['author'],
            #district=data['district'],
        )
        sess.add(kp)
        logger.info(f'{kp} Добавлен в БД')
        sess.commit()


def get_next_number_kp() -> int:
    """Возвращает номер следующего КП."""
    with session() as sess:
        obj = sess.query(
            KontrolPoint,
        ).order_by(
            KontrolPoint.created_at,
        ).all()[-1]
        return obj.number + 1


def get_kp_for_author(author: User) -> list[KontrolPoint]:
    """Список всех КП автора."""
    with session() as sess:
        return sess.query(KontrolPoint).filter(KontrolPoint.author == author).all()
