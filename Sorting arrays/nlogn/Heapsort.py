#Zdefiniujemy drzewo i jego parametry
# tab[0] ma zawierać rozmiar
# ZACZYNAMY OD 1!!
def parent(i):return i//2
def left(i): return i*2
def right(i): return i*2 + 1
def size(k): return k[0]

def heapify(k,i):   #Naprawia kopiec działając w dół!
    #Функция создана для поднятия наибольшего значения в ветке (L,R,Korzeń) 
    #и восстановлению ущерба, причиненного поднятием (то есть опустил меньший элемент ниже 
    # и проверил условие MaxHeap)
    L=left(i)
    R=right(i)
    max=i
    size=k[0]
    if L<=size and k[L]>k[max]:
        max=L
    if R<=size and k[R]>k[max]:
        max=R
    if max!=i:
        k[i],k[max]=k[max],k[i]
        heapify(k,max)
def BuildHeap(tab):
    #Funckja dziala z dołu w górę! (Bo musisz naprawic calkiem kopiec, a naprawiajac z dzieci
    #nie robisz duzo razy to same)
    for i in range(tab[0]//2,0,-1):
        heapify(tab,i)
    return tab
def heapsort(tab):
    #Musimy dolaczyc na poczatek k[0] bo powyzsze funkcje biora to wartosc
    tab = [len(tab)] + tab
    #Budujemy heap
    tab=BuildHeap(tab)
    for _ in range(tab[0],0,-1): 
        #Czyli robimy posortowana tablice od konca przez zmniejszenie range of heapify i swap
        tab[tab[0]],tab[1]=tab[1],tab[tab[0]] #Last now is sorted max
        tab[0]-=1 #Taking into the heapify 1 el less
        heapify(tab,1)
    return tab[1:]
print(heapsort([5,3,1,0,2,4,4,4,5]))







