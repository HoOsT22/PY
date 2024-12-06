try:
    sb = open("pyramida.txt", "w", encoding = "utf-8" )
    cislo = 1

    pocet = int(input("kolik pater bude mit pyramida?: "))
    for x in range(pocet):
        sb.write(" " * (pocet - x) + "*" * (2 * x + 1)+ "\n")
        cislo +=1
        sb.close

except Exception as e:
    print(f"nastala tato chyba: {e}")
finally:
    print("Dekujeme za pouziti naseho zapisniku.")