import time
import vk_api
#vk = vk_api.VkApi(login = 'login', password = 'password')
vk =vk_api.VkApi(token = '7d123bbb8438e07013a06253e265c654d7344cd910ebeb98732ae86d02053d0c51cf255c61ad20c6ed7eb') #Авторизоваться как сообщество

vk._auth_token()

values = {'out': 0,'count': 100,'time_offset': 60}
vk.method('messages.get', values)

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
            write_msg(item[u'user_id'],u'Упс... Что-то пошло не так, попробуйте чуть позже :(')
            print(item[u'user_id'])
    time.sleep(30)

