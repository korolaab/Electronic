import sys
import requests
from xml.dom.minidom import *

def joke(adult):
    x = 1    
    if(adult):
        x = 11
        
    response = requests.get("http://rzhunemogu.ru/Rand.aspx?CType={}".format(x))
    
    
    u = str((response.content).decode('cp1251'))
    #print(type(u))
    #print(u)
    try:
        xml = parseString(u)
        xml.normalize()
        data = xml.getElementsByTagName('content')
    except:
        print("E:", sys.exc_info()[0])
        return "Не могу вспомнить.Напиши попозже :(\nА вообще, иди учи физику, неуч!!!"
    for e in data:
        for t in e.childNodes:
            return(t.data)
