import datetime
"""import os
def check_ping():
    hostname = "vk.com"
    response = os.system("ping -c 4 " + hostname)
    # and then check the response...
    
    #string  = response[84:]

    return response
"""
def timer():
    now = datetime.datetime.now()
    ege = ["география/информатика","математика база","математика профиль","химия, история","русский язык","иностранные языки (устная часть)","обществознание","биология, иностранные языки ","литература, физика "] 
    ege_timer = [datetime.datetime(2018, 5, 28,10,0,0), datetime.datetime(2018, 5, 30,10,0,0),datetime.datetime(2018, 6, 1,10,0,0),datetime.datetime(2018, 6, 4,10,0,0),datetime.datetime(2018, 6, 6,10,0,0),datetime.datetime(2018, 6, 9,10,0,0),datetime.datetime(2018, 6, 14,10,0,0),datetime.datetime(2018, 6, 18,10,0,0), datetime.datetime(2018, 6, 20,10,0,0)]
    string = ['','','','','','','','','']
    
    i = 0
    while i < 9:
        ege_timer[i] = now - ege_timer[i]
        
        string[i] = "{}--{} д {} ч {} мин {} с".format(ege[i],str(ege_timer[i].days),str(ege_timer[i].seconds // 3600),str(ege_timer[i].seconds % 3600 // 60),str(ege_timer[i].seconds % 3600 % 60))
        i = i + 1
    myString = '\n'.join(string)

    return "Все мучения закончились давно)!\n" + myString + ("\nУчитывайте погрешность :)")

#print(timer())
