import numpy as np

def zaliczenie(x=[]):
    print("zadanie 1: liczba studentów którzy nie zaliczyli n przedmoitów")
    c = int(input("podaj liczbę niezaliczonych przedmiotów: "))
    ilu = 0
    for a in x:
        licznik = 0
        for b in a:
            if b < 3.0:
                print(b)
                licznik += 1
        if licznik >= c:
            ilu += 1
    print("Takich studentów jest: ", ilu)
    print()
    return 2

def ocenyśer(x=[]):
    print("zadanie 2: oceny studentów z najnizsza i najwyzsza średnia: ")
    oceny = list()
    mini = round(np.mean(x), 2)
    maks = round(np.mean(x), 2)
    for a in x:
        p = round(np.mean(a), 2)
        # print(p)
        oceny.append(round(np.mean(a), 2))
        if p < mini:
            mini = p
        if p > maks:
            maks = p

    for a in x:
        if round(np.mean(a), 2) == mini or round(np.mean(a), 2) == maks:
            print(a)
    print()
    return 3

def histogram(x=[]):
    print()
    print(4)

    print("zadanie 4: 4 histogram")
    hist, bins = np.histogram(x, bins=[2.0, 3.0, 4.0, 5.0, 5.5])
    print( hist,'\n', bins)
    print()

def najwyzsze(x=[]):
    print("zadanie 3 student z najwyzsza liczba ocen najwyzszych")
    maks = x.max()
    print(maks)
    mkslicz = 0
    for a in x:
        licz = 0
        for b in a:
            if b == maks:
                licz += 1
        if licz > mkslicz:
            return a

def pow4(x=[]):
    print("zadanie 5: studenci z śr >=4.0")

    for a in x:
        srednia = np.mean(a)
        if srednia >= 4.0:
            print(a)


for q in range(2):
    x=np.random.uniform(2.0,high=5.5, size=(5,3)) #lsoowannie macierz 5/3 od liczb od 2.0 do 5.5
    x=np.around(x, decimals=1) #zaokraglanie do 1, miejsca po przecinku
    print(" Ta macierz została wylosowana: ")
    print("LISTA OCEN: ")
    print(x)
    print()



    print(zaliczenie(x))
    print(ocenyśer(x))
    print(najwyzsze(x))
    print(histogram(x))
    print(pow4(x))
