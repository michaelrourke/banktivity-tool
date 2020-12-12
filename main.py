import sqlite3
from datetime import datetime
import csv


def get_maxZPK(table):
    c.execute("SELECT MAX(Z_PK) FROM " + table)
    Z_PK = c.fetchone()[0]
    return Z_PK

def get_primaryKey(item):
    c.execute("SELECT Z_ENT FROM Z_PRIMARYKEY WHERE Z_NAME = ?", (item,))
    Z_ENT = c.fetchone()[0]
    return Z_ENT

def get_securityUniqueId(symbol):
    c.execute("SELECT ZPUNIQUEID FROM ZSECURITY WHERE ZPSYMBOL = ?", (symbol,))
    ZPUNIQUEID = c.fetchone()[0]
    return ZPUNIQUEID

def update_primaryKey(key, i):
    c.execute("UPDATE Z_PRIMARYKEY SET Z_MAX = ? WHERE Z_ENT = ?", (i, key))

def insert_securityPriceItem(ZPUNIQUEID):
    Z_ENT = get_primaryKey("SecurityPriceItem")
    Z_PK = get_maxZPK("ZSECURITYPRICEITEM") + 1
    data = (Z_PK, Z_ENT, 1, None, None, None, ZPUNIQUEID)
    c.execute("INSERT INTO ZSECURITYPRICEITEM VALUES (?, ?, ?, ?, ?, ?, ?)", data)
    update_primaryKey(Z_ENT, Z_PK)
    return Z_PK

def insert_securityPrice(symbol, date, close, i):
    Z_ENT = get_primaryKey("SecurityPrice")
    ZPUNIQUEID = get_securityUniqueId(symbol)
    c.execute("SELECT Z_PK FROM ZSECURITYPRICEITEM WHERE ZPSECURITYID = ?", (ZPUNIQUEID,))
    try:
        ZPSECURITYPRICEITEM = c.fetchone()[0]
    except:
        ZPSECURITYPRICEITEM = insert_securityPriceItem(ZPUNIQUEID)

    Z_PK = i
    # Z_ENT = Z_ENT
    Z_OPT = 1
    ZDATASOURCE = 3
    ZPDATE = (datetime.strptime(date, "%Y/%m/%d") - datetime(1970, 1, 1)).days
    # ZPSECURITYPRICEITEM = ZPSECURITYPRICEITEM
    ZPADJUSTEDCLOSEPRICE = 0
    ZPCLOSEPRICE = close
    ZPHIGHPRICE = 0
    ZPLOWPRICE = 0
    ZPOPENPRICE = 0
    ZPPREVIOUSCLOSEPRICE = 0
    ZPVOLUME = 0

    data = (Z_PK, Z_ENT, Z_OPT, ZDATASOURCE, ZPDATE, ZPSECURITYPRICEITEM, ZPADJUSTEDCLOSEPRICE, ZPCLOSEPRICE, ZPHIGHPRICE, ZPLOWPRICE, ZPOPENPRICE, ZPPREVIOUSCLOSEPRICE, ZPVOLUME)

    c.execute("INSERT INTO ZSECURITYPRICE VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

file_path = ""
csv_path = ""
delimiter = ";"

db = sqlite3.connect(file_path + "/StoreContent/core.sql")
c = db.cursor()

Z_PK = get_maxZPK("ZSECURITYPRICE")

with open(csv_path, 'rt') as csv_in:
    reader = csv.reader(csv_in, delimiter=delimiter)
    next(reader)

    for row in reader:
        Z_PK += 1
        symbol = row[0]
        date = row[1]
        close = row[2]

        insert_securityPrice(symbol, date, close, Z_PK)

Z_ENT = get_primaryKey("SecurityPrice")
update_primaryKey(Z_ENT, Z_PK)

db.commit()
db.close()
