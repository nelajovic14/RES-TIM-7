from email import message
from ntpath import join
import socket
from turtle import end_fill
from typing import List
from WriterClass import Message


def logovanje():
    br = 0
    nijeUlogovan = True
   
    while(nijeUlogovan):
        if(br == 0):
            print("--- POTREBNO JE DA SE ULOGUJETE DA BISTE MOGLI UNOSITI PODATKE ---\n")
            br = 1
        print("Unesite korisničko ime:")
        ime = input()
        print("Unesite šifru:")
        šifra = input()
        
        try:
          fajl = open("korisnici.txt")
        except IOError as e:
            raise IOError("Fajl ne postoji")
            
        lines = [line.strip() for line in fajl]
        for i in lines[2:]:
            (imeKorisnika, prezimeKorisnika, korisničkoIme, šifraKorisnika) = i.split(" ")
            if (ime == korisničkoIme) and (šifra == šifraKorisnika) :
                nijeUlogovan = False
                print("Uspešno ste se ulogovali kao " + imeKorisnika +  " " + prezimeKorisnika)
               
                return(imeKorisnika, prezimeKorisnika) 
        fajl.close()   
        if(nijeUlogovan):
           print("UNELI STE NEISPRAVNO KORISNIČKO IME ILI LOZINKU! POKUŠAJTE PONOVO!")    
    
    
    
    
    

            
def unos_podataka(imeKorisnika, prezimeKorisnika):

    print("--- Unos novih podataka ---- ") 
    print("Unesite ID korisnika: ")
    id = input()

    print("Unesite trenutnu potrošnju vode korisnika: ")
    potrošnja = input()
        
    print("Unesite mesec: ")
    mesec = input()

    Message.__init__(message, id, potrošnja, mesec, imeKorisnika, prezimeKorisnika)
    
    
    return message



def konekcija():
    clientSocket = socket.socket()
    localHost = "127.0.0.1"
    port = 10001

    print("Waiting for connection")

    try:
        clientSocket.connect((localHost, port))
    except socket.error as e:
        print(str(e))

    (imeKorisnika, prezimeKorisnika) = logovanje()
    while True: 
         
        message = unos_podataka(imeKorisnika, prezimeKorisnika)

        clientSocket.send(str.encode(Message.__str__(message)))
        print("Korisnik" + " "+ imeKorisnika + " "+ prezimeKorisnika + " " + " je uspešno poslao podatke.")
    clientSocket.close()
    
konekcija()

