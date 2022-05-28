from KonekcijaKaBazi import *

sqlquery = "select b.ulica, p.mesec, sum(p.potrosnja) as POTROSNJA from brojilo b, potrosnja p where b.idb = p.brojiloid and b.ulica='Micurinova' group by b.ulica, p.mesec"
cursor = con.cursor()
cursor.execute(sqlquery)
rows = cursor.fetchall()
print('Izvestaj za ulicu: ' + str(rows))
