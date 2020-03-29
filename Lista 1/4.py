import numpy as np

def czy_poprawny(a=[], b=[]):
    print("zadanie 1: ")
    q=1
    for x in a:
        try:
            x[1] != b[indeksy[x[1]], 0]
        except:
            print("tego nie ma:  ", x[1])
            q=0
    if q==1:
        print("poprawny")

def zaplata(a=[], b=[]):
    print("Zadanie 2: ")
    n = int(input("podaj nr klienta: "))
    suma = 0
    for a in x:
        towar = a[1]
        ile = a[2]
        if a[0] == n:
            suma += y[indeksy[towar], 1] * ile
            '''print(y[indeksy[a[1]],1])
            print(a[2])'''
    print("Ten klient ma do zapłaty ",suma, " zł")

x = np.array([[1,2,2],[1,5,2],[1,6,1],[1,5,2],[2,7,2],[2,7,1]])# nr klienta | nr towaru | liczba szt.
y = np.array([[5,23,1],[6,33,0],[7,12,1]]) #nr. towaru | cena jed. | info czy na szt/kg
indeksy={5:0, 6:1, 7:2}#znamy indeksy 5 6 7
for q in range(2):
    print(x)
    print()
    print(y)
    print()
    czy_poprawny(x,y)
    zaplata(x,y)
    print()
    print()
