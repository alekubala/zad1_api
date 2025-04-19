
def podejmij_decyzje(wiek, pensja, ocena):
    if wiek > 18 and pensja > 4000 and ocena > 6:
        return "TAK"
    else:
        return "NIE"

decyzja = podejmij_decyzje(25, 5000, 7)
print(f"Decyzja: {decyzja}")
