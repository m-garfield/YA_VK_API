from pprint import pprint
from progress.bar import IncrementalBar
import requests as re
from tqdm import tqdm
def taking_photos(owner_id, count=5):
    with open("token", "r") as file:
        token = file.read().strip()

    base_url = 'https://api.vk.com/method/'                                                 # Базовый адрес обращения к API
    url = 'https://api.vk.com/method/photos.get'                                            # Путь к методу  photos.get
    params_photo_profile = {                                                                # Параметры подгрузки фоток в профиле
        'owner_id': owner_id,
        'album_id': 'profile',
        'extended': '1',
        'access_token': token,
        'count': count,
        'v': '5.131'
    }

    params_photo_wall = {                                                                   # Параметры подгрузки фоток на стене
        'owner_id': owner_id,
        'album_id': 'wall',
        'extended': '1',
        'access_token': token,
        'count': count,
        'v': '5.131'
    }
    photos_list = []
    name_folder = re.get(f'{base_url}users.get?user_ids={owner_id}&access_token={token}&v=5.131').json()
    # photos = re.get(url, params=params_photo_profile).json()
    #
    # if 'error' in photos:
    #     pprint("Пользователь ограничил просмотр своих фотографий профиля")
    # else:
    #     bar = IncrementalBar('Загружаем фото из профиля', max=len(photos['response']['items']))
    #     for photo in photos['response']['items']:
    #         bar.next()
    #         res_photo = {'name': photo['likes']['count'], 'size': photo['sizes'][-1]['type'], 'href': photo['sizes'][-1]['url']}
    #         photos_list.append(res_photo)
    #     bar.finish()
    photos = re.get(url, params=params_photo_wall).json()
    if 'error' in photos:
        pprint("Пользователь ограничил просмотр своих фотографий на стене")
    else:
        bar = IncrementalBar('Загружаем фото стены', max=len(photos['response']['items']))
        for photo in photos['response']['items']:
            bar.next()
            res_photo = {'name': photo['likes']['count'], 'size': photo['sizes'][-1]['type'], 'href': photo['sizes'][-1]['url']}
            photos_list.append(res_photo)
        bar.finish()
    return photos_list, name_folder['response'][0]['last_name']
