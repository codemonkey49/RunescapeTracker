from valueRetrieve import *
from sql import *

def itemAvg(ID,length):
    data=retrieveData(ID,length)
    prices=[]
    #print len(data)
    for i in range(len(data)):
         row= str(data[i])
         #print (row)
         row=(row.split(","))[2]
         #print (row)
         row=int(row.rstrip(")"))
         #print row
         prices.append(row)
    avg= sum(prices)/len(prices)
    return avg
    #for i in range 

def changeRate(ID,length):
    data=retrieveData(ID,length)
    prices=[]
    deltas=[]
    #print len(data)
    for i in range(len(data)):
         row= str(data[i])
         #print (row)
         row=(row.split(","))[2]
         #print (row)
         row=int(row.rstrip(")"))
         #print row
         prices.append(row)
         
    for i in range(len(prices)-1):
        delta=prices[i+1]-prices[i]
        deltas.append(delta)
    #print deltas
    stripped=[]
    for i in range(len(deltas)):
        currentDel=deltas[i]
        if currentDel != 0:
            stripped.append(currentDel)
            
            
    return round(float(sum(stripped))/len(stripped),2)
    #print sum(stripped)
    #print len(stripped)
    #return prices


#print changeRate(440,100)


def checkPurchase(ID):
    longAvg=changeRate(ID,200)
    medAvg=changeRate(ID,25)
    shortAvg=changeRate(ID,10)
    curPrice=fetchPrice(440)
    print longAvg,medAvg,shortAvg,curPrice
    if (medAvg<0)and(shortAvg>1)and(curPrice<longAvg):
        print fetchPrice(ID)[1],"is ready. ","current:",curPrice,"average:",avg
    return ID,longAvg,medAvg,shortAvg
    
x=checkPurchase(440)