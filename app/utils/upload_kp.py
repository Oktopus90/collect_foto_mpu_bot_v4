import csv

from bot.crud.kontrol_point import get_kp_for_author, get_all_kp
from bot.crud.user import get_user_bd_from_tg_id


def save_list_kp(chat_id: int) -> str:
    """Сохраняет csv с КП."""
    author = get_user_bd_from_tg_id(chat_id)
    list_kp = get_all_kp()
    with open(
        f'tmp/{author.username}.csv',
        mode="w",
        encoding='utf-8',
    ) as w_file:
        names = [
            "number",
            "latitude",
            "longitude",
            "adres",
            "comments",
            "question",
            "photo",
            'author',
            'date_create',
        ]
        file_writer = csv.DictWriter(
            w_file,
            delimiter=";",
            lineterminator="\r",
            fieldnames=names,
        )
        file_writer.writeheader()
        for kp in list_kp:
            write_obj = {
                "number": kp.number,
                "latitude": kp.latitude,
                "longitude": kp.longitude,
                "adres": kp.adres,
                "comments": kp.comments,
                "question": kp.question,
                "photo": kp.photo,
                "author": kp.author.username,
                "date_create": kp.created_at,
            }
            file_writer.writerow(write_obj)
    return f'tmp/{author.username}.csv'
