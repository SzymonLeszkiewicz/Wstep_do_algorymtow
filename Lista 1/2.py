import numpy as np

def uzupelnij(n):

    m = n
    b = [[0] * m for i in range(n)]
    a=np.array(b)
    for i in range(n):
        for j in range(n):
            print("podaj liczby", i + 1, "rownania")
            t = int(input())
            a[i,j] = t

    for row in a:
        for elem in row:
            print(elem, end='    ')
        print()
    print()
    return a

def odleglosc(macierz1=[], macierz2=[]):
    print(macierz1)
    print()
    print(macierz2)
    print()

    odl = 0
    for p in range(a):
        for o in range(a):
            odl += abs(macierz1[p, o] - macierz2[p, o])

    print("Odgległość symetryczna wynosi", odl)

for q in range(2):
    a=int(input("czy chcesz sam podać macierz (0/1)? "))
    if a:
        n = int(input("podaj liczbe rownian w ukladnie: "))
        pier=uzupelnij(n)
        drug=uzupelnij(n)
        odleglosc(pier, drug)
    else:
        print("wylosuje ja za Ciebie: ")
        a = 5
        mac1 = np.random.randint(30, size=(a, a))
        mac2 = np.random.randint(30, size=(a, a))
        odleglosc(mac1, mac2)
        print()
