from fileIO import *
from valueRetrieve import *
from data import *
import time
count=0
#1511,1515,1521,1777
IDs=[440,442,444,447,451,453]
while True:
    
    for i in range(len(IDs)):
        #print IDs[i]
        itemID=IDs[i]
        price=fetchPrice(itemID)
        #print price
        if price != "error":
            inputDatabase(itemID,price)
        #checkPurchase(IDs[i])
        time.sleep(1)
    time.sleep(60*60*6)
    count+=6
    print "hours:",count