""" 
Dzmitry Mikialevich
 """

""" 
Pomysl polega na nastep krokach:
    1. Policzyc za pomoca Counting Sorta ilosc Jednokrotnych Cyfr i Wielokrotnych Cyfr -> O(n + 10) i zrobic krotke (liczba,Jednokr,Wielokr) (n - ilosc liczb)
    2. Posortowac liczby Stabilnym Sortowaniem (Counting Sort) najpierw po Wielokrotnych, Potem po Jednokrotnych Cyfrach  ->O(Zl_st_sortowania) -> O(k*n), k - laczna ilosc cyfr w liczbach, n - ilosc liczb
Zlozonosc calego--> O(2*k*n + (n+10))

Uwaga: -> Zlozonosc danego kroku
      --> Zlozonosc algorytmu
 """


def Wielo_Jedno_Krotne(number):
    """ 
    Zmodyfikowany Counting Sort
     """
    if number == 0:
        """ 
        Obsugujemy edge case oddzielnie,
        bo 0 to JednoKrotne
         """
        return [0, 1, 0]
    tab_of_digits = [0] * 10
    to_ret = number
    """ 
    Zbieram cyfry liczby
     """
    while number > 0:
        tab_of_digits[number % 10] += 1
        number = number // 10

    Wielo_Krotne = 0
    Jedno_Krotne = 0
    for i in tab_of_digits:
        if i == 1:
            Jedno_Krotne += 1
        elif i > 1:
            Wielo_Krotne += 1
    return [to_ret, Jedno_Krotne, Wielo_Krotne]


def counting_sort(tab, index):
    n = len(tab)
    to_ret = [0] * n
    max_el = 10
    tab_count = [0] * max_el

    for i in range(max_el):
        tab_count[i] = 0
    for i in range(n):
        tab_count[tab[i][index]] += 1
    for i in range(1, max_el):
        tab_count[i] += tab_count[i-1]
    for i in range(n-1, -1, -1):
        tab_count[tab[i][index]] -= 1
        to_ret[tab_count[tab[i][index]]] = tab[i]
    """ 
    Mozna ewentualnie zwrocic to_ret, ale tak jest wygodniej
     """
    for i in range(n):
        tab[i] = to_ret[i]


def pretty_sort(tab):
    """ Dodaje krotki odrazu dodajac wartosci """
    for i in range(len(tab)):
        tab[i] = Wielo_Jedno_Krotne(tab[i])
    print(tab)
    """ Najpierw dla Wielokrotnych, zeby zachowac stabilnosc """
    counting_sort(tab, 2)
    counting_sort(tab, 1)
    print(tab)


""" 
pretty_sort([114577,2344, 67333]) """
