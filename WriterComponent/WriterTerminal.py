from email import message
from ntpath import join
import socket
from turtle import end_fill
from typing import List
from WriterClass import Message


def Logovanje():
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
        
        fajl =  open("korisnici.txt")
        lines = [line.strip() for line in fajl]
        for i in lines[2:]:
            (imeKorisnika, prezimeKorisnika, korisničkoIme, šifraKorisnika) = i.split(" ")
            if (ime == korisničkoIme) and (šifra == šifraKorisnika) :
                nijeUlogovan = False
                print("Uspešno ste se ulogovali kao " + imeKorisnika +  " " + prezimeKorisnika)
                return(imeKorisnika, prezimeKorisnika) 

        if(nijeUlogovan):
           print("UNELI STE NEISPRAVNO KORISNIČKO IME ILI LOZINKU! POKUŠAJTE PONOVO!")    
     
    fajl.close()    
    
      
       

               
def UnosPodataka(imeKorisnika, prezimeKorisnika):

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

    (imeKorisnika, prezimeKorisnika) = Logovanje() 
    message = UnosPodataka(imeKorisnika, prezimeKorisnika)

    clientSocket.send(str.encode(Message.__str__(message)))
    print("Korisnik" + " "+ imeKorisnika + " "+ prezimeKorisnika + " " + " je uspešno poslao podatke.")

    
    clientSocket.close()


konekcija()

