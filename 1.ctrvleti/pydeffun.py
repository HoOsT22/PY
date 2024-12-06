import random

def rekni():
    print(mp, mj)

jmena = ["Pepa", "Dima", "Jan", "Filip"]
mj = random.choice(jmena)

pozdravy = ["Ahoj", "Zdar", "Čauky"]
mp = random.choice(pozdravy)

rekni()



print("-----------------------------------------------------------------------------------------------------------")




def obvod(a, b):
    c = 2*(a+b)
    return c

def obsah(a, b):
    c = a*b
    return c

for x in range (10):
    strana1 = random.randint(1, 100)
    strana2 = random.randint(1, 100)

    o1 = obvod(strana1, strana2)
    o2 = obsah(strana1, strana2)
    print(f"Obvod obdélníku o stranách {strana1} a {strana2} má obvod {o1}")
    print(f"obsah obdélníka je :  {o2}")



print("-----------------------------------------------------------------------------------------------------------")



def objem(a, b, c):
    S = a*b*c
    return S

strana3 = random.randint(1, 100)
strana4 = random.randint(1, 100)
strana5 = random.randint(1, 100)

o3 = objem(strana3, strana4, strana5)


print(f"Objem obdélníku o stranách {strana3}, {strana4} a {strana5} je: {o3}")



print("-----------------------------------------------------------------------------------------------------------")



def povrch(a, b, c):
    P = 2*(a*b+b*c+a*c)
    return P

strana6 = random.randint(1, 100)
strana7 = random.randint(1, 100)
strana8 = random.randint(1, 100)

o4 = povrch(strana6, strana7, strana8)

print(f"Povrch obdélníku o stranách {strana6}, {strana7} a {strana8} je: {o4}")