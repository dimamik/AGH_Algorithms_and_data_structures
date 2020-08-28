# Hoare polega na częściowym podziale bez ustawienia pivota, więc 
# rozbijając tab musimy włączyć piv_index
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
tab=[17,3,17,20,0,17,0,1,1546,0,15]
Quick_Sort(tab)
print(tab)




















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

#Checker(Quick_Sort,100)