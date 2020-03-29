#wprowadzenie modyfikacji do bubblesorta
import time, sys
def bubblesort1(a=[]):
    '''funkcja do podpunktu 2'''
    n=len(a)#dlugosc tablicy
    for i in range(n):
        przejscie = True
        for y in range(0, n - i - 1):
            if a[y] > a[y + 1]:
                przejscie=False
                a[y], a[y + 1] = a[y + 1], a[y]#zamiana bez dodatkowej zmiennej
        if przejscie == True:#jeżeli w calym przejsciu nie nastapiła zadna zamiana
            print("Nastapilo przerwanie: ")
            return a
    print("nie bylo podstaw do przerwania programu ")
    print()
    return a

def bubblesort2(a=[]):
    '''funkcja do podpunktu 2'''
    n=len(a)#dlugosc tablicy
    for i in range(n):
        for y in range(0, n - 1):#ZA KAZDYM RAZEM DOCHODZIMY DO KONCA TABLICY
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]#zamiana bez dodatkowej zmiennej
    return a

a=list()
try:
    rozmiar=int(input("podaj rozmiar tablicy do posortowania: "))
except:
    print("podales niewlasciwe wartosci: ")
    time.sleep(3)
for x in range(rozmiar):
    try:
        b = int(input("podaj element tablicy:[liczby calkowite] "))
        a.append(b)
    except:
        print("podales niewlasciwe wartosci")
        time.sleep(2)
        sys.exit(0)
print("TWOJA TABLICA WYGLADA NASTEPUJACO: ")
print(a)
print()
print(bubblesort1(a))
print(bubblesort2(a))
print()
print("program zakonczy sie za 5 sekund: ")
time.sleep(5)
