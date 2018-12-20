import sqlite3

def connect():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, date text, store text, amount float)")
    cur.execute("CREATE TABLE IF NOT EXISTS spend (id INTEGER PRIMARY KEY, amounts float)")
    conn.commit()
    conn.close()

def insert(date, store, amount):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO data VALUES (NULL,?,?,?)",(date, store, amount))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(date="", store="", amount=""):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data WHERE date=? OR store=? OR amount=?", (date, store, amount))
    rows=cur.fetchall()
    conn.close()
    return rows

def total_spent():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT SUM(amount) FROM data")
    rows=cur.fetchall()
    conn.close()
    return(rows[0][0])

def delete(id):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM data WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,date, store, amount):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("UPDATE data SET date=?,store=?,amount=? WHERE id=?",(date, store, amount,id))
    conn.commit()
    conn.close()   

def sertin():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO spend (amounts) VALUES (1000.00)")
    conn.commit()
    conn.close()

def dateup(amounts,id=1):
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("UPDATE spend SET amounts=? WHERE id=?",(amounts,id))
    conn.commit()
    conn.close()

def ewvi():
    conn=sqlite3.connect("data.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM spend")
    rows=cur.fetchall()
    conn.close()
    return rows[0][1]



connect()

print(ewvi())

# insert("20-24-1994","Marshalls",26.75)
# print(search(store="Marshalls"))
# update(1,"12-12-2018","Walmart",58.8)
# delete(2)
# delete(4)
# sertin()
# dateup(2100)
# print(total_spent())
# print(total_spent())
# print(ewvi())
# print(view())