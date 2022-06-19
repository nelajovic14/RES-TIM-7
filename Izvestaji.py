from dataclasses import dataclass
from KonekcijaKaBazi import Baza
from FileClass import OpenFile
connection_string='bp1/ftn@localhost'



def izvestaj_ulica(ulica):
    if(isinstance(ulica, str)):
        con = Baza(connection_string)
        sqlquery = "select b.ulica, p.mesec, sum(p.potrosnjaa) as potrosnja from brojilo b, POTROSNJAKORISNIKA p where b.idb = p.brojiloid and b.ulica='"+ulica+"' group by b.ulica, p.mesec"
        rows=con.do_query_with_result(sqlquery)
        print('Izvestaj za ulicu: ' + str(rows))
        f=OpenFile()
        f.open_with_mode("brIzvestaja1.txt","r")
        br=f.read_from_file()
        f.fajl.close()
        brr = int(br)+1
        
        f.open_with_mode("brIzvestaja1.txt", "w")
        f.write_in_file(str(brr))
        f.fajl.close()
        naziv = "IzvestajUlica"+str(br)
        f.open_with_mode(naziv, 'w')
        for x in rows:
            f.write_in_file(x[0] + "   ")
            f.write_in_file(x[1] + "   ")
            f.write_in_file(str(x[2])+ "\n")
        f.fajl.close()
        return True
    else:
        raise TypeError("Uneseni parametar nije string")
    

def izvestaj_brojilo(brojilo):
    if(brojilo.isdigit()): 
        con = Baza(connection_string)
        sqlquery = "select b.idb, p.mesec, sum(p.potrosnjaa) as potrosnja from brojilo b, POTROSNJAKORISNIKA p where b.idb = p.brojiloid and b.idb="+ brojilo +" group by b.idb,  p.mesec"
        rows=con.do_query_with_result(sqlquery)
        print('Izvestaj za brojilo: ' + str(rows))
        f=OpenFile()
        f.open_with_mode("brIzvestaja2.txt","r")
        br=f.read_from_file()
        f.fajl.close()
        brr = int(br)+1
        f.open_with_mode("brIzvestaja2.txt", "w")
        f.write_in_file(str(brr))
        f.fajl.close()
        naziv = "IzvestajBrojilo"+str(br)
        f.open_with_mode(naziv, 'w')
        for x in rows:
            f.write_in_file(str(x[0]) + "   ")
            f.write_in_file(x[1] + "   ")
            f.write_in_file(str(x[2])+ "\n")
        f.fajl.close()
        return True
    else:
        raise TypeError("Uneseni parametar nije broj")

def funkcija_za_izvestaje():
    br = ""
    while(br != "exit"):
        print("Ukoliko zelite izvestaj za ulicu unesite 1, a za brojilo unesite 2, za izlazak exit: ")
        br = input()
        if(br == "1"):
            print("Unesite ulicu: ")
            ulica = input()
            izvestaj_ulica(ulica)
        if(br == "2"):
            print("Unesite id brojila: ")
            brojilo = input()
            izvestaj_brojilo(brojilo)

if __name__ == "__main__":
   funkcija_za_izvestaje()
  
