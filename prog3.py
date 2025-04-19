
import argparse

def podejmij_decyzje(wiek, pensja, ocena):
    if wiek > 18 and pensja > 4000 and ocena > 6:
        return "TAK"
    else:
        return "NIE"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--wiek", type=int, required=True)
    parser.add_argument("--pensja", type=float, required=True)
    parser.add_argument("--ocena", type=float, required=True)

    args = parser.parse_args()
    decyzja = podejmij_decyzje(args.wiek, args.pensja, args.ocena)
    print(f"Decyzja: {decyzja}")
