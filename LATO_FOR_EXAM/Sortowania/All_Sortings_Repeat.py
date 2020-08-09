
tab = [6,5,4,3,2,1,0]
def Bubble_Sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if (tab[j]>tab[i]):
                tab[j],tab[i] = tab[i],tab[j]
    return tab


def Insertion_sort(tab):
    for i in range(1,len(tab)):
        j= i-1
        val = tab[i]
        while (j>=0 and val<tab[j]):
            tab[j+1]=tab[j]
            j-=1
        tab[j+1]=val
    return tab


def Hoares_Partition(tab):
    pivot = tab[len(tab)-1]
    tab_more = []
    tab_less = []
    for i in range(len(tab)-1):
        if (tab[i]<=pivot):
            tab_less.append(tab[i])
        else:
            tab_more.append(tab[i])
    tab_to_ret = tab_less + [pivot]+ tab_more
    for i in range(len(tab)):
        tab[i]=tab_to_ret[i]
    return len(tab_less)

print(Hoares_Partition([6,5,2,1,3,4]))

def QuickSort(tab):
    if (len(tab)<=1):
        return tab
    while (len(tab)>1):
        pivot_index = Hoares_Partition(tab)
        k = tab[:pivot_index]
        f = tab[pivot_index+1:]
        return (QuickSort(k) + [tab[pivot_index]] + QuickSort(f))
    


print(QuickSort(tab))




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
        s=randint(2,15)
        for i in range(s):
            tab.append(randint(0,999))
        return_from_funct=SortingFunc(tab)
        x=sorted(tab)
        if return_from_funct==x:
            print("Test passed")
            positive+=1
        else:
            """ print(return_from_funct,sorted(tab)) """
            print("Test Failed")
    print("ALL TESTS PASSED WITH A SCORE", positive,"/",all)

Checker(QuickSort)