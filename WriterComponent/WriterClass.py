class Message:
    def __init__(self, id, potrošnja, mesec, korisnikIme, korisnikPrezime):
        self.id = id
        self.potrošnja = potrošnja
        self.mesec = mesec
        self.korisnikIme = korisnikIme
        self.korisnikPrezime = korisnikPrezime
        
        
        
    
    def __str__(self):
        return "Server primio podatke od korisnika: "+ self.korisnikIme + " " +  self.korisnikPrezime + "\n" +"id:" + " "+ self.id + "\n" + "potrošnja: "  + ""+ self.potrošnja + "\n" + "mesec: " + self.mesec
