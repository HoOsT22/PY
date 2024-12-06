try:

    sb = open("radkovat.txt", "w", encoding = "utf-8" )
    for x in range(0, 101):
        sb.write(f"Řadek {x}" + "\n")




    
except Exception as e:
    print(f"nastala tato chyba: {e}")
finally:
    print("Dekujeme za pouziti naseho zapisniku.")