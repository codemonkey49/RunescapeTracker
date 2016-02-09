import sqlite3 as lite

con=lite.connect("data.db")

def updateStock(itemID,amt,cost):
    with con:
        cur=con.cursor()
        
    return