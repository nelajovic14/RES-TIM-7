def obrada(poruka):
    redovi_poruke = poruka.split("\n")

    ime_korisnika = redovi_poruke[0].split(": ")[1].split(" ")[0]
    prezime_korisnika = redovi_poruke[0].split(": ")[1].split(" ")[1]
    id = redovi_poruke[1].split(": ")[1]
    potrosnja = redovi_poruke[2].split(": ")[1]
    mesec = redovi_poruke[3].split(": ")[1]
    #print(id + " " + potrosnja + " " + mesec)

    return id, potrosnja, mesec, ime_korisnika, prezime_korisnika