try:
    zapisnik = open("kopie.txt", "wt", encoding = "utf-8")
    while True:
        text = input('>>> ')
        if text.lower()== "konec":
           break
        else:
            zapisnik.write(text+"\n")

    zapisnik.close()
except Exception as e:
    print(f"nastala tato chyba: {e}")
finally:
    print("Dekujeme za pouziti naseho zapisniku.")
    