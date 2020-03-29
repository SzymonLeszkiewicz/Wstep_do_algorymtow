#eliminacja Gaussa
for q in range(2):
    n=int(input("podaj liczbe rownian w ukladnie: "))
    m = n+1
    a = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(n+1):
            print("podaj liczby", i+1 ,"rownania")
            t=int(input())
            a[i][j] = t

    for row in a:
        for elem in row:
            print(elem, end='    ')
        print()

    z=0
    # ELIMINACJA GAUSSAAAAAAAAA
    for k in range(n): # jesli istnieje niebezpieczenstwo dzielenia przez zero
        if a[k][k]==0:
            z= k + 1
            while a[z][k]==0 and z<n: #sprawdzamy czy w kolejnych wierszaqch jest
                z+=1                   #liczba rozna od zera w kolumnie k
            if z==n:
                print("nie ma rozwiazania lub jest nieskonczenie wiele rozwiazan ;/ ")
                break
            else:
                for y in range(k, n + 1):
                    temp = int()
                    temp = a[z][y]
                    a[z][y]= a[k][y]
                    a[k][y]= temp
        for i in range(k + 1, n, 1):
            for j in range(n, -1, -1):
                a[i][j] = a[i][j] - a[i][k] * a[k][j] / a[k][k] #eliminacja wspolczynnikow
    print()


    # wyswietlanie
    for row in a:
        for elem in row:
            if type(elem)==int:
                print(elem, end='    ')
            else:
                print(elem, end=' ')
        print()

