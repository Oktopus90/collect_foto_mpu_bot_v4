import os


def save_photo(chat_id: str, number_kp: int) -> int:
    """Сохраняет фотографии из tmp  в папку."""
    photo_list = os.listdir(f'tmp/{chat_id}')
    count_photo = len(photo_list)
    if not os.path.exists(f'photo/{chat_id}'):
        os.mkdir(f'photo/{chat_id}')
    for number_photo in range(count_photo):
        os.rename(
            f'tmp/{chat_id}/{photo_list[number_photo]}',
            f'photo/{chat_id}/{number_kp}_{number_photo + 1}.jpg'
        )

def remove_tmp_photo(chat_id: str) -> None:
    """Удаление если есть фото тмп."""
    photo_list = os.listdir(f'tmp/{chat_id}')
    for photo in photo_list:
        os.remove(f"tmp/{chat_id}/{photo}")