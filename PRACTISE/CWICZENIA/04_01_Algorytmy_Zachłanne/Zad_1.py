""" 
Dzialanie algorytmu polega na:
1) Wybieranmy zajecie konczace sie najwczesniej
2) Dalej w petli szukamy dla niego sasiadow sposrod wszystkich pozostalych elementow w nasepujacy sposob:
    a)Poczatek szukanego sasiada musi byc wiekszy lub rowny koncu tego, dla ktorego szukamy (Czyli żeby nie nachodziły)
    b)Roznica miedzy koncem sasiada i początkiem tego, dla ktorego szukamy ma byc najmniejsza
3) Kazdy raz jak znalezlismy sasiada to robimy counter++, dalej zwracamy counter
 """
def tasks(A):
    if len(A)==0:return 0
    #Szukamy najmniejszego elementa 
    #(Mozna przechowywac w tablice, ale to nie wplywa na zlozonosc)
    min_end=A[0][1]
    min_first = A[0][0]
    for i in range(len(A)):
        if A[i][1]<min_end:
            min_end=A[i][1]
            min_first=A[i][0]
    #Ustawiamy counter na 1 bo juz wybralismy nasze pierwsze zajecie
    Counter_of_less=1
    for i in range(len(A)):
        #Korzystam tu z wbudowanej nieskonczonosci (ale mozna uzyc 9999 zamiast tego)
        #(Lub ewentualnie ustawic na jakas pierwsza wartosc jak poprzednio)
        min_odl=float('inf') #lub min_odl=999999 
        #Ustawiam na -1 zeby potem sprawdzic czy wchodzilem w drugiego ifa
        tmp_next_first=-1
        tmp_next_end=-1
        #Szukamy zajecia z najmniejszej "Odlegloscia"
        for j in range(len(A)):
            #Sprawdzamy czy nie nachodzi
            if A[j][0]>=min_end:
                #Sprawdzam czy mniej niz poprzeni min
                if A[j][1]-min_first<min_odl:
                    min_odl=A[j][1]-min_first
                    tmp_next_first=A[j][0]
                    tmp_next_end=A[j][1]
        if tmp_next_first!=-1:
            Counter_of_less+=1
            min_first=tmp_next_first
            min_end=tmp_next_end
    return Counter_of_less

    """ Zlozonosc tego algorytmu O(n^2) bo szukamy "minimalnego" sąsiada dla kazdego zajecia (Lub po prostu dla tego, ze mamy zazebiony for), algorytm zachlanny jest poprawny bo sprawdza wszystkie "mozliwe" przypadki (oprocz tego ze ustawia pierwszy element wybierajac najwczesniejszy poczatek, ale to mozna udowodnic w sposob, przedstawiony na wykladzie, ze Jak by istnialo rozwiazanie lepsze bez tego elementu, to juz by nie bylo ono lepszym)"""

# elementarny test, powinien wypisac 2
print( tasks([ (0,10), (10,20), (5,15) ] ))
