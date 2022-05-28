
from WriterClass import Message

def unosPodataka():
    print("---- Unos novih podataka ---- ") 
    print("Unesite ID korisnika: ")
    id = input()

    print("Unesite trenutnu potrosnju vode korisnika: ")
    potrosnja = input()

    Message.__init__(message, id, potrosnja)
    return message

