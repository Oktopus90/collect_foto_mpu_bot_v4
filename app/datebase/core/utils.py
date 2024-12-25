from uuid import uuid4


def generator_random_uuid() -> str:
    """Функция для генерации UUID4 и возрат строки."""
    return str(uuid4())
