from datebase.core.db import session
from datebase.models.kontrol_point import KontrolPoint
from datebase.models.age_category import AgeCategory
from datebase.models.district import District
from utils.logger import get_logger

logger = get_logger(__name__)


def add_kontrol_point(data: dict[str, str]) -> None:
    """Добаление КП в БД.

    Args:
        data (dict): {
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
    data['district'] = District(
        name="Тестовый район",
    )
    data['age_category'] = AgeCategory(
        name="Нет",
        color="нет",
    )
    with session() as sess:
        kp = KontrolPoint(
            adres=data['adres'],
            latitude=float(data['latitude']),
            longitude=float(data['longitude']),
            question=data['question'],
            discription=data['discription'],
            comments=data['comments'],
            photo=str(data['photo']),
            age_category=data['age_category'],
            author=data['author'],
            district=data['district'],
        )
        sess.add(kp)
        logger.info(f'{kp} Добавлен в БД')
        sess.commit()

