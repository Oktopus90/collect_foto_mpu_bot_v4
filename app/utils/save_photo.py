import os

from dotenv import load_dotenv
from utils.additional_functions import enshure_dir
import yadisk

load_dotenv()
YA_TOKEN = os.getenv('YA_TOKEN')

client = yadisk.Client(token=YA_TOKEN)


def save_photo(chat_id: str, number_kp: int) -> int:
    """Сохраняет фотографии из tmp  в папку.

    :param chat_id: Ид пользователя.
    :param number_kp: Номер КП.

    """
    photo_list = os.listdir(f'tmp/{chat_id}')
    count_photo = len(photo_list)
    enshure_dir(f'photo/{chat_id}')
    for number_photo in range(count_photo):

        os.rename(
            f'tmp/{chat_id}/{photo_list[number_photo]}',
            f'photo/{chat_id}/{number_kp}_{number_photo + 1}.jpg',
        )


def upload_folder_to_yadisk(path_folder: str) -> list[str]:
    """Выгрузка файлов из папки на Ядиск.

    :param path_folder: Путь к папки из коорой надо все выгрузить.
    """
    list_files = os.listdir(path_folder)
    result = []
    with client:
        for file in list_files:
            client.upload(path_folder + '/' + file, 'photo_test/' + file)
            result.append(file)
    return result


def remove_tmp_photo(chat_id: str) -> None:
    """Удаляет фто из папки tmp по chat_id.

    :param chat_id: Ид пользователя.
    """
    photo_list = os.listdir(f'tmp/{chat_id}')
    for photo in photo_list:
        os.remove(f"tmp/{chat_id}/{photo}")
