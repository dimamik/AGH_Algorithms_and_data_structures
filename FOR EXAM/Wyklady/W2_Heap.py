def parent(i): return i//2
def left(i): return i*2
def right(i): return i*2 + 1
def size(k): return k[0]


def heapify_max(tab,i):
    """ 
    Procedura, naprawiająca kopiec
     """
    """ 
    Find max from kids
     """
    l=left(i)
    r=right(i)
    max_i=i
    size_of_tab=size(tab)
    if size_of_tab>0 and size_of_tab<len(tab) and l<=size_of_tab:
        if tab[max_i]<tab[l]:
            max_i=l
    if size_of_tab>0 and size_of_tab<len(tab) and r<=size_of_tab:
        if tab[max_i]<tab[r]:
            max_i=r
    if max_i!=i:
        tab[max_i],tab[i]=tab[i],tab[max_i]
        heapify_max(tab,max_i)

def BuildHeap(tab):
    for i in range(size(tab),0,-1):
        heapify_max(tab,i)
    return tab

def reverse_tab(tab):
    new_tab=[0]*len(tab)
    curr_i=0
    for i in range(len(tab)-1,-1,-1):
        new_tab[curr_i]=tab[i]
        curr_i+=1
    return new_tab

def HeapSort(tab):
    tab_to_ret=[]
    tab=[len(tab)]+tab
    tab=BuildHeap(tab)
    while size(tab)!=0:
        tab_to_ret.append(tab[1])
        tab[1],tab[size(tab)]=tab[size(tab)],tab[1]
        tab[0]-=1
        heapify_max(tab,1)
    tab_to_ret=reverse_tab(tab_to_ret)
    return tab_to_ret

from random import *
def Checker(SortingFunc,k):
    positive=0
    all=k
    for i in range(k):
        tab=[]
        s=randint(10,99)
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



Checker(HeapSort,150)


print(HeapSort([6,5,4,3,2,1]))
""" print(HeapSort([1,2,3]))
print(BuildHeap([2,6,8,1,5,7,4])) """

        
