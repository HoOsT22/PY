sb = open("vizitka.txt", "w", encoding = "utf-8" )
jmeno = input("Zadej jmeno:")
delka = len(jmeno)
    
sb.write("*" * (delka + 12) + "\n")
sb.write("******" + jmeno + "******" + "\n")
sb.write("*" * (delka + 12) + "\n")
print("*" * (delka + 12) )
print("******" + jmeno + "******")
print("*" * (delka + 12) )
