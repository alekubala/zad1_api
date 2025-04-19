
wiek = int(input("Podaj wiek: "))
pensja = float(input("Podaj pensję: "))
ocena = float(input("Podaj ocenę: "))

if wiek > 18 and pensja > 4000 and ocena > 6:
    decyzja = "TAK"
else:
    decyzja = "NIE"

print(f"Decyzja: {decyzja}")