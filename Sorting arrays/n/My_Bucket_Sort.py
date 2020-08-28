# Pomocniczy QuickSort
def Hoare_part(tab,low,high):
    pivot=tab[low]
    i=low-1
    j=high+1
    while 1:
        while 1:
            i+=1
            if tab[i]>=pivot:break
        while 1:
            j-=1
            if tab[j]<=pivot:break
        # Jesli indeksy nie nachodza to swap
        if i<j:
            tab[i],tab[j]=tab[j],tab[i]
        else:
        #wracamy wartosc j ktora jest ustawiona na el kotory "presortowany"
            return j

def Quick_Sort(tab,low=0,high=-1):
    """ 
    Main:
        Niestabilny, O(nlogn) -> O(n^2)
        Pracuje z danej tablicej
    Algorithm:
        Rozdziela dane na pre-sorted groups wzgl pivota
    Zastosowania:
        Summa from i to j -> Find i el and j el and then go throught tab adding ->(O(n))
        k-th smallest
     """
    if high==-1:
        high=len(tab)-1
    if low<high:
        piv_idex=Hoare_part(tab,low,high)
        Quick_Sort(tab,low,piv_idex)
        Quick_Sort(tab,piv_idex+1,high)
    return tab

def Bucket_Sort(tab, n=False):

    """ Dziala tylko dla jednostajnego rozkladu danych z przedzialu
    [0,k], k - max(tab)
    Stabilny -> O(n) dla rozk?adu jednostajnego
    Zeby znalezc liczbe bucketow:

    Rozdielnosc Bucketa -> parametr dla najlepszego rozkladu
    Im lepiej rozklad, tym mniej zlozonosc 
    Rozd Bucketa ->       max_el/ilosc_elementow
    Ilosc Bucketow ->     Max_el/rozd_Bucketa=ilosc_elementow
    ind Bucketa dla el -> El/rozd_Bucketa

    Mozna dodac normalizacje: Przesuniecie wszystkich elementow tak, zeby byly od 0 """
    max_el = max(tab)
    if n == False:
        n = len(tab)

    rozd_Bucketa = max_el/len(tab)
    Buckets = [[] for _ in range(n+1)]
    for number in tab:
        index_of_Bucket = int(number/rozd_Bucketa)
        #add using insertion sort in bucket (but in this case just add)
        Buckets[index_of_Bucket].append(number)
    for i in range(n+1):
        Buckets[i] = Quick_Sort(Buckets[i])
    to_return = []
    for i in range(n+1):
        for j in range(len(Buckets[i])):
            to_return.append(Buckets[i][j])
    return to_return


print(Bucket_Sort([0.1, 0.2, 0.05, 0.15, 1]))
















""" TESTING """
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

#Checker(Bucket_Sort,1000)