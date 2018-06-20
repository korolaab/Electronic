


def load():
    ids = []
    #names =[]
    us_id = ''
    f = open("id",'r')
    users = f.read()
    n = 0
    

    for i in users:        
        if(n >= 17):
            break     
        if( i != '\n'):
            us_id = us_id + i            
        elif(i == '\n' ):
            n += 1        
            ids.append(us_id)
            us_id = ''
    f.close
    return ids

def add(user_id):
    f = open("id",'a')
    f.write(str(user_id) + '\n')
    f.close
    

#print (ids)
#print (names)
