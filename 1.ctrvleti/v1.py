# ošetření výjimečných stavů programu
try: # tady testujeme výjimky
    c1 = input("Zadej cislo : ")
    c1 = float(c1)
    c2 = c1/0

except ZeroDivisionError:
    print("Nulou se nesmi delit")


except Exception as e: # tady řešíme co se stane, když nastane chyba
    print(f"neco se rozbilo, nastala chyba {e}")


finally: # proběhne vždycky
    print("a je to konec")