from pprint import pprint
import requests
from taking_photos import taking_photos
from ya_disk import Yandex_disk

owner_id = input("Введите ID пользователя: ")
count = input("Введите количество фотографий: ")
ya_token = None
with open("ya_token", "r") as file:
    ya_token = file.read().strip()


list_photos, name_folder = taking_photos(owner_id, count)


yad = Yandex_disk(ya_token, name_folder, list_photos)

yad.upload_file()












#href_file = 'https://sun9-17.userapi.com/c871/u00001/-7/x_8e0ca14e.jpg'






