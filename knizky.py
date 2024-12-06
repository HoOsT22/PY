try:
    import json
    soubor = open ("knihy.json", "rt" , encoding="utf-8" )
    slovnik = json.load(soubor)
    print(type(slovnik))
    for klic, hodnota in slovnik.items(): 
        print(f'Kniha s id: {klic}')
        print(f'Nazev knihy: {hodnota["nazev"]}')
        print(f'Autor: {hodnota["jmeno_autora"] + ["prijmeni_autora"]}')
        print(f'Zanr knihy:{hodnota["zanr"]}')
        print(f'Pocet stran: {hodnota["pocet_stran"]}')
    soubor.close()
except Exception as e:
    print (f"Nastala chyba: {e} ")
finally:
    print(f"Konec programu...")