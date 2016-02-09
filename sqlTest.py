import sqlite3 as lite
con=lite.connect("data.db")
with con:
    cur=con.cursor()
    

    #cur.execute("CREATE TABLE stuff(id INT,name TEXT,price INT)")
    #cur.execute("INSERT INTO stuff VALUES(1,'ironOre',220)")
    #print "1"
    #cur.execute("INSERT INTO priceData VALUES(1,440,269)")
    #print "2"
    #cur.execute("DELETE FROM priceData WHERE itemID=449")
    #cur.execute("SELECT * FROM priceData WHERE ID=440")
    cur.execute("SELECT * FROM priceData")
    #inputDatabase(440,200)
    #cur.execute("SELECT * FROM priceData ORDER BY i DESC LIMIT 1")
    rows= cur.fetchall()
    for row in rows:
        print (row)