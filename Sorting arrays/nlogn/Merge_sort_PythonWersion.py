""" Wersja pythonowska Merge_sorta """


def merge(l, r):
    # O(n)
    i_l = 0
    i_r = 0
    tab_to_ret = []
    while i_l < len(l) and i_r < len(r):
        if l[i_l] < r[i_r]:
            tab_to_ret.append(l[i_l])
            i_l += 1
        else:
            tab_to_ret.append(r[i_r])
            i_r += 1
    while i_l < len(l) and i_r >= len(r):
        tab_to_ret.append(l[i_l])
        i_l += 1
    while i_l >= len(l) and i_r < len(r):
        tab_to_ret.append(r[i_r])
        i_r += 1
    return tab_to_ret


def Merge_sort(tab):
    """ 
    Stabilny -> O(nlogn) -> O(nlogn)
    Divide and Concure
     """
    if len(tab) == 1:
        return tab
    if len(tab) > 1:
        med = len(tab)//2
        return merge(Merge_sort(tab[:med]), Merge_sort(tab[med:]))


print(Merge_sort([78,15,12,32,15,2,0,1,0]))



""" TESTING MODULE """
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



#Checker(Merge_sort,100)