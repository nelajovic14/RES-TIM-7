def obrada(poruka):
    try:
        redovi_poruke = poruka.split("\n")

        id_korisinka = redovi_poruke[1].split(": ")[1]
        potrosnja = redovi_poruke[2].split(": ")[1]
        mesec = redovi_poruke[3].split(": ")[1]

        return id_korisinka + ", " + potrosnja + ", " + mesec
    except IndexError:
        raise IndexError("Index out of the range")
        