import time, random, sys #time do mierzenia czasu oraz wstrzymywanie programu random to losowania liczb sys do zamykania
from statistics import mean #srednia
try:
    q=int(input("Podaj ile elementow ma miec lista do posortowania: "))
    b=int(input("Podaj dolna granice zakresu z ktorego ma byc losowana liczba: "))
    c=int(input("Podak gorna granice zakresu: "))
except:
    print("podano niepoprawna wartosc !")#wstrzymywanie programu w razie podania wartosci nie calkowitych
    print("program zakonczy dzialanie za 5 sek ")
    time.sleep(5)
    sys.exit(0)
print("******************************************")
print()
czasy=list() #tworzenie listy na pomiary czsów
maks_bubble=0 #zmienna przechowywujaca maks czas

for pow in range(10): # losowanie 10 ciagów
    a = list() #pusta lista na wylosowane wartosci
    for x in range(q):
        a.append(random.randint(b,c))#losowanie liczb calkowitych z podanego zakresu
    start=time.time() #zmienna na czas początkowy
    #sortowanie bąbekowe
    for x in range(len(a)-1, 0, -1):
        for y in range(0, x):
            if a[y]>a[y+1]:
                a[y], a[y+1]=a[y+1], a[y] #zamiana wartosci bez uzywania zmiennej tymczasowej
    stop=time.time() #zmienna na czas koncowy
    czas=stop-start #obliczanie czas wykonywania
    czasy.append(czas)#dodawanie pomiaru do listy
    if czas>maks_bubble:#wyznaczanie maks czasu
        maks_bubble=czas
print("****BUBBLESORT****")
print("Średni czas: ", mean(czasy))# obliczanie średniego czasu Bubble
print("Maksymalnu czas: ", maks_bubble)



czasy=[]
maks_wybor=0
for pow in range(10): # losowanie 10 ciagów
    a =[] #pusta lista na wylosowane wartosci
    for x in range(q):
        a.append(random.randint(b,c))#losowanie liczb calkowitych z podanego zakresu
    start=time.time() #zmienna na czas początkowy
    #sortowanie przez wybor
    for i in range(0, len(a)):
        k=i
        for j in range(i+1, len(a)):# w tej petli szukamu indeksu najmniejszego elementu
            if a[j]<a[k]:          #znajdującego się najblizej poczatku tablicy
                k=j
        a[k], a[i]=a[i],a[k]# zamiana wartosci bez uzywania zmiennej pomocniczej
    stop=time.time() #zmienna na czas koncowy
    czas=stop-start #obliczanie czas wykonywania
    czasy.append(czas)#dodawanie pomiaru do listy
    if czas > maks_wybor:
        maks_wybor=czas
print()
print("****SORTOWANIE PRZEZ WYBOR****")
print("Średni czas: ", mean(czasy))
print("Maksymalny czas: ", maks_wybor)
print()
print("PROGRAM ZAKONCZY DZIAŁANIE ZA 10 SEKUND")
time.sleep(10)