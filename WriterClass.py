class Message:
    def __init__(self, id, potrosnja, mesec, korisnik_ime, korisnik_prezime):
        self.id = id
        self.potrosnja = potrosnja
        self.mesec = mesec
        self.korisnik_ime = korisnik_ime
        self.korisnik_prezime = korisnik_prezime
        
        
        
    
    def __str__(self):
        return "Server primio podatke od korisnika: "+ self.korisnik_ime + " " +  self.korisnik_prezime + "\n" +"id:" + " "+ self.id + "\n" + "potrošnja: "  + ""+ self.potrosnja + "\n" + "mesec: " + self.mesec
