import time
import vk_api
from termcolor import colored
import users_methods
import _thread
import string
import fun
import sys
import EGE_timer as EGE

status = False
users = users_methods.load()
AY = u"1321442"
admin_id = u'167890754'   
string = ""
name = ""
def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})
i = 0
find = False



status = ['', '']

import disk

def hi():
    a = u"Привет :)"
    return a


def help():
    a = u'Доступные команды:\n"--help" помощь\n "dz" или "дз" ссылки на домашнее задание.\nЕсли станет скучно набери "анекдот"\n"--version" версия электроныча'
    return a


def dz():
    global status
    #disk.check_disk(drive)
    a = ''
   # if(status[0] !='i'and status[1] !='f'):
      #  a = u"Прости, но дз еще не выложено, хотя ты его так жаждешь =)"
        #return a
    a = u'Физика:\nhttps://drive.google.com/drive/folders/1bjmpOkawtodicQ25ZWWp02p6B9kla9qb\n\n\nИнформатика:\nhttps://drive.google.com/drive/folders/1dXuvEiVZdUCjWcoQPwYc7EvpKOU1PEG1'
    return a


admin = False
temp_user = ""
def alien_check(users,user_id):
    global temp_user
    global admin
    i = 0
    while i < len(users):
        if(users[i] == user_id or user_id == AY):
            
            admin = False
            return admin
        i += 1 
    
    write_msg(admin_id,u'Неизвестный в дом постучал https://vk.com/id{}\nДобавить его в дом наш?[y/n]'.format(user_id))
    temp_user = user_id
    admin = True
    
    return admin
    
def admin_commands(string,user_id):
    global temp_user
    global admin  
    global users
    
         
    if(string == u'y' ):
        
        users.append(temp_user)
        users_methods.add(temp_user)
        admin = False
        
        a = u'[OK]Пользователь https://vk.com/id{} добавлен'.format(temp_user )
        temp_user = ""
    elif(string == u'n' ):
        a = u'[OK]Игорить пользователя https://vk.com/id{}'.format(temp_user)
        admin = False
    else:
        a = u'Требуется ввести "y" или "n"'
    return a

def answer(string,user_id):
    user_id = str(user_id)
   
    global admin
    global users

    string = string.lower()
    
    
    if(admin and (user_id == admin_id)):
        
        return admin_commands(string,user_id)
        

    if(alien_check(users,user_id)):
        return "Я тебя не знаю =("  
    
    
        
       
         

    if(string == u"дз" or string == u"dz"):
        return dz()
    if(string == u"привет"):
        return hi()
    if(string == u"--help"):
        return help()
    if(string == u"--version"):
        return("0.06/2beta\nДата запуска 10.03.18")
    if(string == u"анекдот"):
        return fun.joke(False)

    if(string == u"анекдот 18++"):
        return fun.joke(True)
    if(string == u"егэ" or string == u"20!8"):
        return EGE.timer()

    
    return u":)"
error = False
def norm(vk):
    values = {'out': 0,'count': 100,'time_offset': 60}

    print("VK_part_started" + colored("[ok]",'green'))
    global error
    while True: 
            global status        
            try:
                response = vk.method('messages.get', values)
            except:
                error = True
                print("E:", sys.exc_info()[0])

                break
            if response['items']:
                values['last_message_id'] = response['items'][0]['id']
                
            for item in response['items']:
                
                write_msg(item[u'user_id'],answer(item[u'body'],item[u'user_id']))
                #print(u'M:"{0:^1}" from id{1:^1} ----{2:^1}' .format(item[u'body'], item[u'user_id'], time.asctime() ) )

            status = disk.get_status()
            if (status[1] =='f' ):
                for i in users:        
                    write_msg(i,u"ДЗ по физике выложено! https://drive.google.com/drive/folders/1bjmpOkawtodicQ25ZWWp02p6B9kla9qb")
                    time.sleep(1)
                write_msg(AY,u"ДЗ по физике выложено! https://drive.google.com/drive/folders/1bjmpOkawtodicQ25ZWWp02p6B9kla9qb")
                print("Physics is notificated")
                

            if (status[0] == 'i'):
                for i in users:        
                    write_msg(i,u"ДЗ по информатике выложено! https://drive.google.com/drive/folders/1dXuvEiVZdUCjWcoQPwYc7EvpKOU1PEG1")
                    time.sleep(1)
                write_msg(AY,u"ДЗ по информатике выложено! https://drive.google.com/drive/folders/1dXuvEiVZdUCjWcoQPwYc7EvpKOU1PEG1")
                print("info is notificated")
 
            disk.resume_status()





#vk = vk_api.VkApi(token = "740686c0883498da758a21bc6d26733a5d503ff8aa2deed45ef058d07688e18b529a47b5ba060c4dfbbd7") #test
vk = vk_api.VkApi(token = "7d123bbb8438e07013a06253e265c654d7344cd910ebeb98732ae86d02053d0c51cf255c61ad20c6ed7eb") #Авторизоваться как сообщество
#vk_api.VkApi(login = 'login', password = 'password')
vk._auth_token()
#drive = disk.auth()




_thread.start_new_thread(disk.load_dz,())
def start(vk):
    global error
    while True:
        if error:
            error = False
            print("W:Restarting vk part:")
        norm(vk)


start(vk)

    


    
                
                
                
              
                
            
            
                

            
    
