sb = open("texty.txt", "rt", encoding = "utf-8" )
kopie = open("kopie.txt", "wt", encoding = "utf-8" )

obsah = sb.read()
print(obsah)

kopie.write(obsah.upper())

sb.close()
kopie.close()

soubor.write("nejaký text \n")