def zadej_cislo():
    while True:
        try:
            cislo = float(input("zadej cislo: "))
            print(f"zadal jsi cislo: {cislo}")
            return cislo
        except Exception as e:
            print(f"chyba : {e}")

vysledek = zadej_cislo()
print(vysledek)