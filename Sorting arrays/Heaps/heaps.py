

""" Defenitions for heap from 0 withot size in arr[0] """

def parent(i):return (i-1)//2
def left(i): return (i*2)+1
def right(i): return (i*2) + 2

def heapify_max_from0(tab,i):
    """ 
    Working with heap from 0 index
     """
    L=left(i)
    R=right(i)
    max=i
    #Size is showing the last index
    size=len(tab)-1
    if L<=size and tab[L]>tab[max]:
        max=L
    if R<=size and tab[R]>tab[max]:
        max=R
    if max!=i:
        #In this place should be struct switch if working with structs
        tab[i],tab[max]=tab[max],tab[i]
        heapify_max_from0(tab,max)
    return tab

def heapify_min_from0(tab,i):
    """ 
    Working with heap from 0 index
     """
    L=left(i)
    R=right(i)
    min=i
    #Size is showing the last index
    size=len(tab)-1
    if L<=size and tab[L]<tab[min]:
        min=L
    if R<=size and tab[R]<tab[min]:
        min=R
    if min!=i:
        #In this place should be struct switch if working with structs
        tab[i],tab[min]=tab[min],tab[i]
        heapify_min_from0(tab,min)
    return tab
#Build heap (change heapify to needed)
def BuildHeap_from_0(tab):
    """     
    Zwykła tablica bez size w tab[0]
    Funckja dziala z dołu w górę! (Bo musisz naprawic calkiem kopiec, a naprawiajac z dzieci
nie robisz duzo razy to same) 
"""
    n=len(tab)-1
    for i in range((n//2)-1,-1,-1):
        heapify_max_from0(tab,i)
    return tab



""" Definitions with heap from 1 """

def parent_from_1(i):return i//2
def left_from_1(i): return i*2
def right_from_1(i): return i*2 + 1
def size(k): return k[0]

def heapify_max_from1(k,i):   
    """ Naprawia kopiec działając w dół!
    Функция создана для поднятия наибольшего значения в ветке (L,R,Korzeń) 
    и восстановлению ущерба, причиненного поднятием (то есть опустил меньший элемент ниже 
     и проверил условие MaxHeap) """
    L=left_from_1(i)
    R=right_from_1(i)
    max=i
    size=k[0]
    if L<=size and k[L]>k[max]:
        max=L
    if R<=size and k[R]>k[max]:
        max=R
    if max!=i:
        k[i],k[max]=k[max],k[i]
        heapify_max_from1(k,max)

def BuildHeap_from_1(tab):
    """ 
tab[0] ma zawierac size,
Funckja dziala z dołu w górę! (Bo musisz naprawic calkiem kopiec, a naprawiajac z dzieci
nie robisz duzo razy to same)
     """
    for i in range(tab[0]//2,0,-1):
        heapify_max_from1(tab,i)
    return tab
    
def Heapsort(tab):
    """ 
    Takes:
        Usual tab
    Returns:
        Sorted tab
    Niestabliny -> O(nlogn) -> (Heapify -> logn, Build Heap -> n)
    Algorithm:
        Buduję kopiec i od końca stosuje Heapify na początku żeby znaleźć wartość największą, potem zamieniam z końcem i zmniejszam range of heapify
     """
    """ 
    !!HEAPSORT GAREK!!
    Takes usual tab as an input and addes size as a tab[0] in O(n) time
     """
    tab = [len(tab)] + tab
    #Budujemy heap
    tab=BuildHeap_from_1(tab)
    for _ in range(tab[0],0,-1): 
        #Czyli robimy posortowana tablice od konca przez zmniejszenie range of heapify i swap
        tab[tab[0]],tab[1]=tab[1],tab[tab[0]] #Last now is sorted max
        tab[0]-=1 #Taking into the heapify 1 el less
        heapify_max_from1(tab,1)
    return tab[1:]

print(Heapsort([5,1,2,7,13,0,15]))



    