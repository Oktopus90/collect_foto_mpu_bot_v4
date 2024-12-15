from datebase.core.db import session
from datebase.models.user import User
from utils.logger import get_logger

logger = get_logger(__name__)


def add_user(data: dict[str, str]) -> None:
    """Добаление пользователя в БД.

    Args:
        data (dict): {
            'username': User name из Tg
            'first_name': first_name name из Tg
            'last_name': last_name name из Tg
            'telegram_id': telegram_id name из Tg
        }.

    Returns:
        None.

    """
    with session() as sess:
        user = User(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            telegram_id=int(data['telegram_id']),

        )
        sess.add(user)
        logger.info(f'{user} Добавлен в БД')
        sess.commit()
