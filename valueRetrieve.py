import urllib2

def fetchPrice(itemID):     #takes the numericID of the item, returns the item's current price, item name
        url='http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='
        full=url[:73] + str(itemID)    #creates a url by combining the item number and the url
        #print full
        response = urllib2.urlopen(full)
        #print response.info()
        html = response.read()
        #print len(html)
        #html=""
        if html=='':
                return "error"
        parsedPieces= html.split('","')   #splits the data from the website at the commas, seperating the pieces
        
        #try:
        #print "trying"
        typeCheck=parsedPieces[2].split(":")[2]
        #print typeCheck
        if typeCheck=='"Mining and Smithing':
                price=parsedPieces[7]
                price=price.split(",")[0]
                price=price.split(":")[1]
                price=price.rstrip("}")
                if ("k" in price):
                        #print price
                        price=price.replace("k","")
                        price=price.replace('"','')
                        price=int(float(price)*1000)
                        #print price
                return price
        #except:
                #return "error"
        # if parsedPieces==['']:
        #         finalValue=0
        #         finalName="error"
        # else:
        #         #print parsedPieces[2]   #item number identifier
        #         #parsedPieces[1]#item image
        #         #print parsedPieces[4]   #item name
        #         #print parsedPieces[7]   #item trend
        #         #print parsedPieces[8]   #item value
        #         response.close()  # best practice to close the file
        #         #print "start"
        #         for i in range (len(parsedPieces)):
        #                 #print parsedPieces[i]
        #                 if "price" and "today" in parsedPieces[i]:
        #                         priceLocation=i
        #                         #print parsedPieces[i]
        #                         #print parsedPieces[i+2]
        #                 if "name" in parsedPieces[i]:
        #                         nameLocation=i
        #                         #print parsedPieces[i]
        #                 #print parsedPieces[i]
        #         try:
        #                 priceLocation
        #         except:
        #                 print parsedPieces,itemID
        #         valuePartial=parsedPieces[priceLocation]    #item value, with junk
        #         #print valuePartial
        #         valuePartial2=valuePartial.split(":")         #item value, without perceeding junk, with extra bracket
        #         #print valuePartial2
        #         finalValue=valuePartial2[1].replace(",","")
        #         finalValue=finalValue.replace("}","")
        
        #         if "k" in finalValue:
        #                 finalValue=((finalValue.split('""')[0]).replace("k",""))
        #                 finalValue=finalValue.replace('"','')
        #                 try:
        #                         finalValue=int(float(finalValue)*1000)
        #                 except ValueError:
        #                         finalValue=0
        #                         finalName="error"
        #                         return(finalValue,finalName)
        #         else:
        #                 try:
        #                         finalValue=int(finalValue.split('"')[1])
        #                 except:
        #                         finalValue=int(finalValue.split('"')[0])
        #         #print finalValue
        #         #finalValue=finalValue.replace(",","")
                
        #         valuePartial=parsedPieces[nameLocation]    #item value, with junk
        #         #print valuePartial
        #         valuePartial2=valuePartial.split(":")         #item value, without perceeding junk, with extra bracket
        #         finalName=valuePartial2[1].replace("}","")
        # return (finalValue),finalName
        
#print fetchPrice(449)
#IDs=[440,436,442,447,1073,1127,557,554,556,1511,1515,1521,1777]
#1511,1515,1521,1777
