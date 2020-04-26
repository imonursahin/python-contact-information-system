#Veritabanı Bilgileri

import sqlite3
def create():
    con = sqlite3.connect("vt.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS iletisim(id INTEGER PRIMARY KEY,ad TEXT,mobil TEXT, mail TEXT,adres TEXT)")
    con.commit()
    con.close()
def viewall():
    con = sqlite3.connect("vt.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM iletisim")
    rows = cur.fetchall()
    con.close()
    return rows

def search(ad="",mobil="",mail="",adres=""):
    con = sqlite3.connect("vt.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM iletisim WHERE ad=? OR mobil=? OR mail=? OR adres=?",(ad,mobil,mail,adres))
    rows = cur.fetchall()
    con.close()
    return rows
def add(ad,mobil,mail,adres):
    con = sqlite3.connect("vt.db")
    cur = con.cursor()
    cur.execute("INSERT INTO iletisim VALUES(NULL,?,?,?,?)",(ad,mobil,mail,adres))
    con.commit()
    con.close()
def update(id,ad,mobil,mail,adres):
    con = sqlite3.connect("vt.db")
    cur = con.cursor()
    cur.execute("UPDATE iletisim SET ad=?,mobil=?,mail=?,adres=? WHERE id=?",(ad,mobil,mail,adres,id))
    con.commit()
    con.close()
def delete(id):
    con = sqlite3.connect("vt.db")
    cur = con.cursor()
    cur.execute("DELETE FROM iletisim WHERE id=?",(id,))
    con.commit()
    con.close()
create()
