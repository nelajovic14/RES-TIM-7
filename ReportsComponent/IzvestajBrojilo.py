from KonekcijaKaBazi import *

sqlquery = "select * from brojilo"
cursor = con.cursor()
cursor.execute(sqlquery)
rows = cursor.fetchall()