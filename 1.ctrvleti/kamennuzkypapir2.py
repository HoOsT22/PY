import random
moznosti = ["kámen", "nůžky", "papír"]
vysledky = []
skore_hrac1 = 0
skore_hrac2 = 0
def urci_viteze(hrac1, hrac2):
    if hrac1 == hrac2:
        return 0  # Remíza
    elif (hrac1 == "kámen" and hrac2 == "nůžky") or \
         (hrac1 == "nůžky" and hrac2 == "papír") or \
         (hrac1 == "papír" and hrac2 == "kámen"):
        return 1  # Vyhrál hráč 1
    else:
        return 2  # Vyhrál hráč 2

for i in range(10):
    hrac1 = random.choice(moznosti)
    hrac2 = random.choice(moznosti)
    vysledek = urci_viteze(hrac1, hrac2)
    
    if vysledek == 1:
        skore_hrac1 += 1
        vysledky.append(f"Hráč 1: {hrac1}, Hráč 2: {hrac2} -> Vyhrál hráč 1")
    elif vysledek == 2:
        skore_hrac2 += 1
        vysledky.append(f"Hráč 1: {hrac1}, Hráč 2: {hrac2} -> Vyhrál hráč 2")
    else:
        vysledky.append(f"Hráč 1: {hrac1}, Hráč 2: {hrac2} -> Remíza")

print("Výsledky jednotlivých her:")
for i, vysledek in enumerate(vysledky, 1):
    print(f"Hra {i}: {vysledek}")

print(f"\nCelkové skóre:")
print(f"Hráč 1: {skore_hrac1} vítězství")
print(f"Hráč 2: {skore_hrac2} vítězství")


skore_hrac1 = 0
skore_hrac2 = 0
for vysledek in vysledky:
    if "Vyhrál hráč 1" in vysledek:
        skore_hrac1 += 1
    elif "Vyhrál hráč 2" in vysledek:
        skore_hrac2 += 1

