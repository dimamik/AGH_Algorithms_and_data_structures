def Lomuto_part(tab,low,high):
    pivot = tab[high]
    curr_index=low-1
    for i in range(low,high):
        if tab[i]<=pivot:
            curr_index+=1
            tab[i],tab[curr_index]=tab[curr_index],tab[i]
    tab[curr_index+1],tab[high]=tab[high],tab[curr_index+1]
    return curr_index+1


def QuickSelect(tab,k,start=0,end=-1):
    """ 
    Znajduje wartosc pod (k-tym indeksem)+1 w posortowanej tablice
    k in [1,len(tab)]
    Zwraca None jeśli k nie pasuje warunkom wyzej
     """
    if k>len(tab) or k<=0 :
        return None
    if end==-1:
        end=len(tab)-1
    pivot_index=Lomuto_part(tab,start,end)
    if k-1==pivot_index-start:
        return tab[pivot_index]
    if k-1>pivot_index-start:
        """ Wchodze w prawo """
        return QuickSelect(tab,k-pivot_index+start-1,pivot_index+1,end)
    else:
        return QuickSelect(tab,k,start,pivot_index-1)
    return None

print(QuickSelect([2,5,1,8,3,6,0,0,0],4))

""" TESTING MODULE"""
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
        k=randint(0,len(tab)-1)
        return_from_funct=SortingFunc(tab,k+1)
        if return_from_funct==sorted(tab)[k]:
            print("Test passed")
            positive+=1
        else:
            """ print(return_from_funct,sorted(tab)) """
            print("Test Failed")
    print("ALL TESTS PASSED WITH A SCORE", positive,"/",all)

#Checker(QuickSelect,100)


