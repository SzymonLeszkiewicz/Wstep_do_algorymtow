import time, random, sys #time do mierzenia czasu oraz wstrzymywanie programu random to losowania liczb sys do zamykania
from statistics import mean #srednia
def bubblesort1(a=[]):
    for x in range(len(a)-1, 0, -1):
        for y in range(0, x):
            if a[y]>a[y+1]:
                a[y], a[y+1]=a[y+1], a[y]
def bubblesort2(a=[]):
    n = len(a)  # dlugosc tablicy
    for i in range(n):
        przejscie = True
        for y in range(0, n - i - 1):
            if a[y] > a[y + 1]:
                przejscie = False
                a[y], a[y + 1] = a[y + 1], a[y]  # zamiana bez dodatkowej zmiennej
        if przejscie == True:  # jeżeli w calym przejsciu nie nastapiła zadna zamiana
            return a
def bubblesort3(a=[]):
    n=len(a)#dlugosc tablicy
    for i in range(n):
        for y in range(0, n - 1):#ZA KAZDYM RAZEM DOCHODZIMY DO KONCA TABLICY
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]#zamiana bez dodatkowej zmiennej
    return a


try:
    q=int(input("Podaj ile elementow ma miec lista do posortowania: "))
    w=int(input("Podaj dolna granice zakresu z ktorego ma byc losowana liczba: "))
    e=int(input("Podak gorna granice zakresu: "))
except:
    print("podano niepoprawna wartosc !")#wstrzymywanie programu w razie podania wartosci nie calkowitych
    print("program zakonczy dzialanie za 5 sek ")
    time.sleep(5)
    sys.exit(0)
print("******************************************")
print()
czasy=list() #tworzenie listy na pomiary czsów

for pow in range(1): # losowanie 10 ciagów
    a = list()  # pusta lista na wylosowane wartosci bubble sort 1
    b = list()  # pusta lista na wylosowane wartosci bubble sort 2
    c = list()  # pusta lista na wylosowane wartosci bubble sort 3
    for x in range(q):#losowanie liczb calkowitych z podanego zakresu
        a.append(random.randint(w, e)) # dla 1 bubble sorta
        b.append(random.randint(w, e))  # dla 2 bubble sorta
        c.append(random.randint(w, e))  # dla 3 bubble sorta

    start1=time.time()   #zmienna na czas początkowy
    bubblesort1(a) #sortowanie bąbekowe wersja 1
    stop1 = time.time()  # zmienna na czas koncowy

    start2=time.time() #sortowanie bąbekowe wersja 2 (z przerywaniem w przypadku braku zamiany elem.)
    bubblesort2(b)
    stop2 = time.time()

    start3 = time.time() #sortowanie bąbekowe wersja 3 (z wykonywaniem sie do konca tablicy)
    bubblesort3(c)
    stop3 = time.time()

    czas1 = stop1 - start1 #obliczanie czas wykonywania bubble sorta 1
    czas2 = stop2 - start2  # obliczanie czas wykonywania bubble sorta 2
    czas3 = stop3 - start3  # obliczanie czas wykonywania bubble sorta 3

    print("***BUBBLESORT 1***")
    print(czas1)
    print()
    print("***BUBBLESORT 2***")
    print(czas2)
    print()
    print("***BUBBLESORT 3***")
    print(czas3)
    print()
    print("program zakonczy dzialanie za 5 sek")
    time.sleep(5)
