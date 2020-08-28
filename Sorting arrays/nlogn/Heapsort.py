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
    """ 
    More in folder HEAP in Sorting Arrays
    Heap -> Satisfies property that if P is parent of Q, than P is more than Q (for MaxHeap)
    Funckja dziala z dołu w górę! (Bo musisz naprawic calkiem kopiec, a naprawiajac z dzieci
    nie robisz duzo razy to same) """
    for i in range(tab[0]//2,0,-1):
        heapify(tab,i)
    return tab
def heapsort(tab):
    """ 
    Takes:
        Usual tab
    Returns:
        Sorted tab
    Niestabliny -> O(nlogn) -> (Heapify -> logn, Build Heap -> n)
    Algorithm:
        Buduję kopiec i od końca stosuje Heapify na początku żeby znaleźć wartość największą, potem zamieniam z końcem i zmniejszam range of heapify
     """
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









""" TEST MODULE """
from random import *
import time
def Timer(func):
    def wrapper(*args,**kwargs):
        tic = time.perf_counter()
        output=func(*args,**kwargs)
        toc = time.perf_counter()
        print(toc)
        return output
    return wrapper
@Timer
def Checker(SortingFunc,k=150):
    positive=0
    all=k
    for i in range(k):
        tab=[]
        s=randint(10,999)
        for i in range(s):
            tab.append(randint(0,999))
        return_from_funct=SortingFunc(tab)
        if return_from_funct==sorted(tab):
            print("Test passed")
            positive+=1
        else:
            """ print(return_from_funct,sorted(tab)) """
            print("Test Failed")
    print("ALL TESTS PASSED WITH A SCORE", positive,"/",all)



#Checker(heapsort,100)





