from contextlib import nullcontext
import logging
import cx_Oracle
import socket
from KonekcijaKaBazi import Baza
from konekcija import Konekcija

def konekcija():
    konekcija=Konekcija(10003,"127.0.0.1")
    konekcija.connect()
    poruka_provera=""
    while True:
        poruka=konekcija.get_poruka()
        
        print("poruka je "+poruka)
        if poruka=="exit":
            break
    
        if poruka!="":
            id_brojila=poruka.split(',')[0]
            try:
                id_brojila=int(id_brojila)
            except TypeError:
                raise TypeError("ID is not int")
            potrosnja=poruka.split(',')[1]
            try:
                potrosnja=int(potrosnja)
            except TypeError:
                raise TypeError("Potrosnja is not int")
                
            mesec=poruka.split(',')[2]
            if poruka_provera!=poruka:
                upis_u_bazu(id_brojila,potrosnja,mesec)
            
            print("Upisano u bazu")
            poruka_provera=poruka
    konekcija.close()
    return True

def konekcija_ka_bazi():
    con = cx_Oracle.connect('bp1/ftn@localhost')
    print("konekcija ka bazi")
    print(con)
    if con == nullcontext:
        raise ValueError("Nemoguca konekcija sa bazom")
    return con

def id_potrosnje():
    con=konekcija_ka_bazi()
    sqlquery="select count(*) from POTROSNJA"
    cursor = con.cursor()
    cursor.execute(sqlquery)   
    n = cursor.fetchall()
    print(n)
    n=n[0][0]
    n=int(n)
    print(n)
    return n

def provera_id(id,mesec):
    con=konekcija_ka_bazi()
    cursor = con.cursor()
    sqlquery="select IME from BROJILO where Idb="+str(id)
    cursor.execute(sqlquery)
    n=cursor.fetchall()
    print(n)
    if n ==[]:
        return False

    sqlquery="select RBPOTROSNJE from POTROSNJA where mesec="+'\''+mesec+'\''+" and BROJILOID="+str(id)
    cursor.execute(sqlquery)
    m=cursor.fetchall()

    if m==[]:
        return True
    else:
        return False
    
        


def upis_u_bazu(id,potrosnja,mesec):
    
    if mesec not in ["januar","februar","mart","april","maj","jun","jul","avgust","septembar","oktobar","novembar","decembar"] :
        raise NameError("Neispravan mesec")
        
    br=id_potrosnje()
    br+=1
   
    baza=Baza('bp1/ftn@localhost')
    if(provera_id(id,mesec)):
        query="INSERT INTO POTROSNJA VALUES ("+str(br)+","+str(id)+","+str(potrosnja)+",\'"+str(mesec)+"\')"
        baza.do_query(query)
        return True
    return False


konekcija()