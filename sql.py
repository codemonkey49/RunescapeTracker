import sqlite3 as lite

#print lite.version

con=lite.connect("data.db")

def inputDatabase(ID,price):
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM priceData ORDER BY i DESC LIMIT 1")
        rows= cur.fetchall()
        try:
            rows=str(rows[0])
            rows=rows.split(",")
            i=int((rows[0].split("("))[1])
        except IndexError:
            i=0
        
        cur.execute("INSERT INTO priceData VALUES(?,?,?)",(i+1,ID,price))
        print "added",i+1,ID,price
        
        
def retrieveData(ID,length):
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM priceData WHERE itemID=440 ORDER BY i DESC LIMIT %s" % (length))
        rows= cur.fetchall()
        return rows
#print retrieveData(440,5)

#with con:
    #cur=con.cursor()
    

    #cur.execute("CREATE TABLE stuff(id INT,name TEXT,price INT)")
    #cur.execute("INSERT INTO stuff VALUES(1,'ironOre',220)")
    #print "1"
    #cur.execute("INSERT INTO priceData VALUES(1,440,269)")
    #print "2"
    #cur.execute("DELETE FROM priceData WHERE itemID=449")
    #cur.execute("SELECT * FROM priceData WHERE ID=440")
    #cur.execute("SELECT * FROM priceData")
    #inputDatabase(440,200)
    #cur.execute("SELECT * FROM priceData ORDER BY i DESC LIMIT 1")
    #rows= cur.fetchall()
    #for row in rows:
        #print row
    
    