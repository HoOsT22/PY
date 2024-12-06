try:
    with open ("ppl.png", "rb") as f:
        obsah = f.read()
    # print(obsah)

except Exception as e:
    print(f"Chybicka se vloudila: {e}")
finally:
    print("Dekujeme za pouziti naseho programu.")