import os
from termcolor import colored

#from pydrive.drive import GoogleDrive
#from pydrive.auth import GoogleAuth
import time

status = ['','']


def get_status():
	global status
	return status

def resume_status():
	global status
	status[0] = ''
	status[1]= ''
           
def load_dz():
    print("Disk part started" + colored("[OK]",'green'))
    while True:
        glazovikovirivatel()


def glazovikovirivatel():
    print("W:Sync Disk--" + colored(time.asctime(),'red'))  
    global status
    f = open("numbers",'r')
    numbers = " "
    numbers = f.read()
    num = [ '' , '' ]
    n = 0
    for i in numbers: 
        if( i != '\n' ):
            num[n] = num[n] + i
        else:
            n = n + 1
    fiz_num = int(num[0])
    info_num = int(num[1])
       
    f.close()
    os.system("grive -p /home/alex/Documents/Electronych/google -s /Школа")
    fiz_list = os.listdir("/home/alex/Documents/Electronych/google/Школа/Физика/ДЗ")
    info_list = os.listdir("/home/alex/Documents/Electronych/google/Школа/Информатика/Дз по информатике")

    
    
    status = ['','']

    if(len(info_list) > info_num):
       status[0] = 'i'
       info_num = len(info_list) 
       print("info is ready")        
       
    if(len(fiz_list) > fiz_num):
        status[1] = 'f'
        fiz_num = len(fiz_list)
        print("fiz is ready")
    
    f = open("numbers","w")
        
    
    f.write(str(fiz_num) +'\n')
    f.write(str(info_num) + '\n')
    f.close()
    
    print("Physics: {} $$$ Informatics: {}".format(len(fiz_list),len(info_list)))
    time.sleep(900)  
    



