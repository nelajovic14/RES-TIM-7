from cmath import e
from contextlib import nullcontext
from msilib.schema import Error
from ntpath import join
import socket
from turtle import end_fill
from typing import List

from WriterClass import Message
from KonekcijaWriter import KonekcijaClient


def otvori_fajl(fajl):
    try:
        otvoreni_fajl = open(fajl)
    except FileNotFoundError:
        print("Fajl ne postoji!")
        return -1
    return otvoreni_fajl  
   

def splitovanje(red_u_fajlu):
    try:
      ime =  red_u_fajlu.split(" ")[0]
      prezime = red_u_fajlu.split(" ")[1]
      korisnicko_ime = red_u_fajlu.split(" ")[2]
      sifra = red_u_fajlu.split(" ")[3]
    except IndexError:
        raise IndexError("Index out of the range")
    return (ime, prezime, korisnicko_ime, sifra)
    

    
def logovanje():
    br = 0
    nije_ulogovan = True
    while(nije_ulogovan):
        if(br == 0):
            print("--- POTREBNO JE DA SE ULOGUJETE DA BISTE MOGLI UNOSITI PODATKE ---\n")
            br = 1
        print("Unesite korisničko ime:")
        ime = input()
        print("Unesite šifru:")
        sifra = input()
        fajl =  otvori_fajl("korisnici.txt")
        lines = [line.strip() for line in fajl]
        for i in lines[2:]:
            (ime_korisnika, prezime_korisnika, korisnicko_ime, sifra_korisnika) = splitovanje(i)
            if (ime == korisnicko_ime) and (sifra == sifra_korisnika) :
                nije_ulogovan = False
                fajl.close() 
                print("Uspešno ste se ulogovali kao " + ime_korisnika +  " " + prezime_korisnika)
                return(ime_korisnika, prezime_korisnika) 
          
        if(nije_ulogovan):
            fajl.close() 
            return("","")  
    
def provera_ispravnosti_podataka(id_korisnika, potrosnja, mesec):
    try:
        int(id_korisnika)
    except ValueError:
       print("Id korisnika mora biti broj.Pokusajte ponovo!")
       return False
   
    try:
        int(potrosnja)
    except ValueError:
       print("Potrosnja korisnika mora biti broj.Pokusajte ponovo!")
       return False
    if mesec not in ["januar", "februar", "mart", "april", "maj", "jun", "jul", "avgust", "septembar", "oktobar", "novembar", "decembar"]:
       print("Uneli ste nepostojeci mesec. Pokusajte ponovo!")
       return False
    return True  
       

               
def unos_podataka(ime_korisnika, prezime_korisnika):
    
  
    while True:
        print("--- Unos novih podataka ---- ") 
        print("Unesite ID korisnika: ")
        id_korisnika = input()
        print("Unesite trenutnu potrošnju vode korisnika: ")
        potrosnja = input()
        print("Unesite mesec: ")
        mesec = input()
        if provera_ispravnosti_podataka(id_korisnika,potrosnja, mesec):
            message=Message(id_korisnika, potrosnja, mesec, ime_korisnika, prezime_korisnika)
            return message

def konekcija():
    konekcija=KonekcijaClient(10001,'127.0.0.1')
    konekcija.connect()
 
    ime_korisnika=""
    prezime_korisnika=""
    while((ime_korisnika, prezime_korisnika)==("","")):
        (ime_korisnika, prezime_korisnika) = logovanje() 
    
    while True:  
        
        message = unos_podataka(ime_korisnika, prezime_korisnika)
        konekcija.send(message.__str__())
        print("Korisnik" + " "+ ime_korisnika + " "+ prezime_korisnika + " " + " je uspešno poslao podatke.")

if __name__=="__main__":
    konekcija()

