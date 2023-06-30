import logging

import requests as req
from progress.bar import IncrementalBar




class Yandex_disk:
    def __init__(self, ya_token, name_folder, list_photos):
        self.name_folder = name_folder
        self.ya_token = ya_token
        self.list_photos = list_photos

    URL = 'https://cloud-api.yandex.net/v1/disk/'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth y0_AgAAAABu-ZBmAADLWwAAAADmfU-DRavVgx5jROWnLeJLM--uIfd-Ic0'
    }
    # создание папки с именем  name_folder
    def upload_file(self):
        req.put(f'{self.URL}resources?path={self.name_folder}', headers=self.headers).json()
        bar = IncrementalBar("Загружаем фотографии на диск", max=len(self.list_photos))
        for photo in self.list_photos:
            bar.next()
            name_file = photo['name'] # Имя файла
            href_file = photo['href'] #Путь к файлу
            path_for_upload = req.get(f'{self.URL}resources/upload?path={self.name_folder}/photo_with_like_{name_file}.jpg', headers=self.headers).json()
            # upload_file = req.post(path_for_upload['href'])
            result = req.post(f'{self.URL}resources/upload?url={href_file}&path={self.name_folder}/{name_file}.jpg', headers=self.headers).json()


        bar.finish()

