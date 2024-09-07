import requests
from pprint import pprint
import json
import os
# https://<адрес-сервера>/method/<имя-API-метода>?<параметры>

class VK:
    VKurl = 'https://api.vk.com/method/'
    Yandexurl = 'https://cloud-api.yandex.net/v1/disk/resources'
    
    def __init__(self, VKtoken, user_id, version='5.199'):
        self.token = VKtoken
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}
        
    def users_info(self):
        params = {'user_ids': self.id}
        response = requests.get(f'{self.VKurl}users.get', params={**self.params, **params})
        return response.json()
    
    def users_photos(self):
        integer_id = (_id['id'] for _id in vk.users_info()['response'])
        params = {'owner_id': integer_id}
        photo_request = requests.get(f'{self.VKurl}photos.get', params={
            **self.params,
            **params,
            'album_id' : 'profile',
            'count' : '5',
            'extended' : 'likes',
            'rev': '0'
        })
        for photo in photo_request.json()['response']['items']:
            image_url = photo['orig_photo']['url']
            file_name = f'{photo['likes']['count']}.jpg'
            for size in photo['sizes']:
                if size['height'] == photo['orig_photo']['height']:
                    info_ = {
                            "file_name": f'{file_name}',
                            "size": size['type']
                                     }
            headers = {
                    'Authorization': YAtoken
                }
            response = requests.put('https://cloud-api.yandex.net/v1/disk/resources/',
                                        params={'path': 'Image'},
                                        headers=headers
                                        )
            response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload', 
                                        params={'path': f'Image/{file_name}'},
                                        headers=headers
                                        )
            url_upload = response.json()['href']                  
            with open(f'{photo['likes']['count']}.json','w+') as info:
                json.dump(info_, info) 
            with open(f'{file_name}', 'wb') as f:
                f.write(requests.get(image_url).content)
            with open(f'{file_name}', 'rb') as f:
                requests.put(url_upload, params={'file': file_name})
                p = os.path.abspath(file_name) 
                print (p)
            
        return f

            


        
YAtoken = 'y0_AgAAAAA7aZKfAADLWwAAAAEP_q_OAAAVEK0cl1JLhJoyyjipo0S-DtpARA'
VKtoken = 'vk1.a.f8VVXWgFKiXNywEkXTZXQCF7_9jhcVOCdtqQjh5utQ_U00gvSYRdheezf0yOH09O4hWB3TLX0TuOHmfmkCdO_Ieq7OThMwBqhiyz4C-bSzDTuxxG6qtE7Z5nzEW-9N2g4451FoYIodDCd6MTKYYyyTN6sHDPGpVfK23vPdgMPXARX85QrVTK_S25JiZKM4R6'
user_id = 'imakuren'
vk = VK(VKtoken, user_id)

print(vk.users_info())
pprint(vk.users_photos())