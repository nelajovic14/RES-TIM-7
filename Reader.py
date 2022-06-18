from contextlib import nullcontext
import logging
import cx_Oracle
import socket
from KonekcijaKaBazi import Baza
from konekcija import Konekcija

connection_string='bp1/ftn@localhost'

def splitovanje_parametara_za_bazu(poruka):
    try:
        id_brojila=poruka.split(',')[0]
        potrosnja=poruka.split(',')[1]
        mesec=poruka.split(',')[2]
    except IndexError:
        raise IndexError("Index out of the range") 
    try:
        id_brojila=int(id_brojila)
        potrosnja=int(potrosnja)
    except ValueError:
        raise ValueError("Vrednosti nisu dobrog tipa")      
    
    if mesec not in ["januar","februar","mart","april","maj","jun","jul","avgust","septembar","oktobar","novembar","decembar"]:
        raise ValueError("Month is not correct")
    return(id_brojila,potrosnja,mesec)
            

def konekcija():
    konekcija=Konekcija(10003,"127.0.0.1")
    konekcija.bind()
    konekcija.connect()
    poruka_provera=""
    while True:
        poruka=konekcija.get_poruka()
    
        print("poruka je "+poruka)

        if poruka!="":
            id_brojila,potrosnja,mesec=splitovanje_parametara_za_bazu(poruka)
            if poruka_provera!=poruka:
                upis_u_bazu(id_brojila,potrosnja,mesec,connection_string)
            
            poruka_provera=poruka


def provera_id(id,mesec):
    sqlquery="select IME from BROJILO where Idb="+str(id)
    baza=Baza(connection_string)
    n=baza.do_query_with_result(sqlquery)
    print(n)
    if n ==[]:
        return False

    sqlquery="select BROJILOID from POTROSNJAKORISNIKA where mesec="+'\''+mesec+'\''+" and BROJILOID="+str(id)
    m=baza.do_query_with_result(sqlquery)

    if m==[]:
        return True
    else:
        return False
    

def upis_u_bazu(id,potrosnja,mesec,connection_string):   
    baza=Baza(connection_string)
    if(provera_id(id,mesec)):
        query="INSERT INTO POTROSNJAKORISNIKA VALUES ("+str(id)+","+str(potrosnja)+",\'"+str(mesec)+"\')"
        baza.do_query(query)
        print("Upisan je podatak u bazu!")
    else:
        print("Podatak nije upisan u bazu!")
        
if __name__=="__main__":
    konekcija()