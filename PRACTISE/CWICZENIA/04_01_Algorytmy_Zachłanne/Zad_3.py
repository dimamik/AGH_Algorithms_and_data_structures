""" Algorytm polega na:
1) Zrobieniu tablicy i przypisywaniu wartosci iz tuple i dodatkowe dodanie miejsca dla wartosci profit=(val/curr_weight), O(n)
2) Wartosc value/curr_weight pozwala nam wybrac najlepsze z punktu widzenia profitu, który może zostać uzyskany w momencie teraźniejszym plecak
3) Sortujemy malejąco względem val/curr_weight (który sie znajduje w tab[i][3])
4) Dalej iterujemy po posortowanej tablicy i:
    a) Bierzemy cały płyn jeżeli się mieści i dodajemy jego val do wyniku
    b) Jeżeli się nie mieści to bierzemy jego część która zapełnia nam cały plecak i dodajemy 
    (k/curr_weight) * curr_val do wyniku (Bo to jest właśnie ta część val którą zabierzemy razem z weight)
(Uwaga!   val - to wartosc P, curr_weight - to pojemnosc W )


 """
def knapsack(A, k):
    if len(A)==0:return 0
    if k==0:return 0
    #Budujemy tablice z tupple
    tab=[[0]*3 for _ in range(len(A))]
    for i in range(len(A)):
        tab[i][0]=A[i][0]
        tab[i][1]=A[i][1]
    #Dodajemy val/curr_weight na koncu kazdego "przedmiotu"
    for i in range(len(A)):
        tab[i][2]=(tab[i][0]/tab[i][1])
    #Sortujemy malejąco względem val/curr_weight 
    #(Za pomocą lambdy pokazujemy że chcemy wzgl 3 el)
    tab=sorted(tab,key=lambda tab: tab[2],reverse=True)
    value_to_ret=0
    #Iterujemy po tab
    for i in range(len(tab)):
        curr_weight=tab[i][1]
        curr_value=tab[i][0]
        if k-curr_weight>=0:
            #Jak sie miesci
            k-=curr_weight
            value_to_ret+=curr_value
        else:
            #Jak nie
            fraction = k/curr_weight
            value_to_ret+=curr_value*fraction
            k=int (k-(curr_weight*fraction))
            #Breakujemy, bo napewno nie mamy więcej miejsca
            break
    return value_to_ret

""" Złożoność przedstawionego algorytmu: O(nlogn) i zależy od algorymtu sortowania
Algorytm jest zachłanny, bo jesteśmy pewni że biorąc element który bierzemy uzyskujemy największy profit (I nie będzie sytuacji że jakiś z małym profitem (val/curr_weight) tak naprawdę jest lepszy (Np (val=2,weight=2),(val=3,weight=4): i mamy do uzupełnienia 5 kg, w tym przypadku powyższy algorytm (po usunieciu fractional part) zwroci val=2, bo profit z pierwszego jest większy niż profit z drugiego. Czyli w naszym problemie, w którym możemy brać części przedmiotów takiej sytuacji być nie może"""


# elementarny test, powinien wypisać 12
print( knapsack( [ (1,1), (10,2), (6,3) ], 3))