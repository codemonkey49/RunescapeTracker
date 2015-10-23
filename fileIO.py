#replaced by sql.py
def inputDatabase(ID,price):
    file=open("database","a+")
    
    file.write(str(ID))
    file.write(";")
    file.write(str(price))
    file.write(",")
    file.write("\n")
    return

def retrieveData(ID):
    price=list()
    itemID=list()
    
    file=open("database","r")
    
    full=file.readlines()
    file.close()
    #print full[0]
    for i in range(0,len(full)):
        #print full[i]
        parsed=full[i].rstrip('\n')
        tempPrice=(parsed.split(";")[1]).split(",")[0]
        tempID=parsed.split(";")[0]
        if tempID==str(ID):
            price.append(tempPrice)
    return(price)
#print retrieveData(556)