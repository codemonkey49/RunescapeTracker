import urllib.request

def fetchData(itemID):     #takes the numericID of the item, returns the item's current price, item name
        url='http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item='
        full=url[:73] + str(itemID)    #creates a url by combining the item number and the url
        response = urllib.request.urlopen(full)
        html = str(response.read())

        #if html=='':
        #        return "error"
        name=(html.split(',')[5])
        name=name.split(":")[1].replace('"',"")

        itemType=(html.split(',')[3])
        itemType=itemType.split(":")[1].replace('"',"")

        price=(html.split(':')[14])
        price=price.split("}")[0].replace('"',"")
        price=price.replace(",","")

        if ("k" in price):
                price=float(price.strip("k"))
                price=int(price*1000)

        return (name,itemType,price)


def fetchPrice(itemID):
        dat=fetchData(itemID)
        return (dat[2])

#print(fetchPrice(2363))
#addy:449
#runite:451