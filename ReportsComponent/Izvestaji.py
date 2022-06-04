from dataclasses import dataclass
from KonekcijaKaBazi import *



def IzvestajUlica(ulica):
    sqlquery = "select b.ulica, p.mesec, sum(p.potrosnjaa) as POTROSNJA from brojilo b, potrosnja p where b.idb = p.brojiloid and b.ulica='"+ulica+"' group by b.ulica, p.mesec"
    cursor = con.cursor()
    cursor.execute(sqlquery)
    rows = cursor.fetchall()
    print('Izvestaj za ulicu: ' + str(rows))
    f = open("brIzvestaja1.txt", "r")
    br = f.read()
    brr = int(br)+1
    f = open("brIzvestaja1.txt", "w")
    f.write(str(brr))
    naziv = "IzvestajUlica"+str(br)
    f = open(naziv, 'w')
    for x in rows:
        f.write(x[0] + "   ")
        f.write(x[1] + "   ")
        f.write(str(x[2])+ "\n")

def IzvestajBrojilo(brojilo):
    sqlquery = "select b.idb, p.mesec, sum(p.potrosnjaa) as POTROSNJA from brojilo b, potrosnja p where b.idb = p.brojiloid and b.idb="+ brojilo +" group by b.idb,  p.mesec"
    cursor = con.cursor()
    cursor.execute(sqlquery)
    rows = cursor.fetchall()
    print('Izvestaj za brojilo: ' + str(rows))
    f = open("brIzvestaja2.txt", "r")
    br = f.read()
    brr = int(br)+1
    f = open("brIzvestaja2.txt", "w")
    f.write(str(brr))
    naziv = "IzvestajBrojilo"+str(br)
    f = open(naziv, 'w')
    for x in rows:
        f.write(str(x[0]) + "   ")
        f.write(x[1] + "   ")
        f.write(str(x[2])+ "\n")


print("Ukoliko zelite izvestaj za ulicu unesite 1, a za brojilo unesite 2: ")
br = input()
if(br == "1"):
    print("Unesite ulicu: ")
    ulica = input()
    IzvestajUlica(ulica)
if(br == "2"):
    print("Unesite id brojila: ")
    brojilo = input()
    IzvestajBrojilo(brojilo)
