seznam = ["ja","krokodyl","tomas","zidle","kravina","mango","wifina","notas","mys","tablet","jablko"]
seznam2 = ["cokolada","krokodyl","gambrinus","slon","kravina","banan","wifina","meme","mys","prst","kolo"]
seznam3 = []
seznam4 = []
#
for polozka in seznam:
    if polozka in seznam2:
        print(polozka)
#
for x in seznam:
    if x not in seznam2:
        seznam3.append(x.upper())
for x in seznam2:
    if x not in seznam:
        seznam3.append(x.upper())
print (seznam3)
#
for x in seznam3:
    slovo = ""
    for pismeno in x:
        slovo+=pismeno+"*"
    seznam4.append (slovo)
for x in seznam4:
    print(x)

