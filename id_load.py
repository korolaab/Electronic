


def load
ids = []
#names =[]
us_id = ''
f = open("id",'r')
users = f.read()
n = 0
l = 0
isIdReady = False
for i in users:
    print(n)
    if(n >= 17):
        break     
    if( i != '\n'):
        us_id = us_id + i            
    elif(i == '\n' ):
        n += 1        
        ids.append(us_id)
        us_id = ''
#print (ids)
#print (names)
