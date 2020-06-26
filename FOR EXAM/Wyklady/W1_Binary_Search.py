def BinarySearch(tab,el_to_search,l=0,r=-1):
    """ 
    O(logn)
     """
    if r==-1:
        r=len(tab)-1
    if l<r:
        mid = (l+r)//2
        if tab[mid]==el_to_search:
            return mid
        elif tab[mid]<el_to_search:
            return BinarySearch(tab,el_to_search,mid+1,r)
        elif tab[mid]>el_to_search:
            return BinarySearch(tab,el_to_search,l,mid)
    if tab[l]==el_to_search:
        return l
    else:
        return -1

""" print(BinarySearch([0,1,2,3,4,5,6,7,8,9,10],10)) """

def BinarySearchIterative(tab,el_to_search):
    l=0
    r=len(tab)-1
    while l<r:
        mid = (l+r)//2
        if tab[mid]==el_to_search:
            return mid
        elif tab[mid]<el_to_search:
            l=mid+1
        elif tab[mid]>el_to_search:
            r=mid
    if tab[l]==el_to_search:
        return l
    else:
        return -1

""" print(BinarySearchIterative([0,1,2,3,5],5)) """


def Insert_In_Sorted_Using_BinarySearch(tab, el_to_insert, l=0, r=-1):
    """ 
    NOT WORKING
    Wstawia element niezaleznie od tego czy jest duplikatem
     """
    if r == -1:
        r = len(tab)-1
    while l+1 < r:
        print("I am in")
        mid = (l+r)//2
        if tab[mid] < el_to_insert:
            l = mid+1
            continue
        if tab[mid] > el_to_insert:
            r = mid
            continue
    
    print(l, r)

Insert_In_Sorted_Using_BinarySearch([1,2,3,5,7],9)



""" 
TO GENERATE RANDOM TAB AND CHECK IF BINARY SEARCH IS WORKING

from random import *
def To_Check_Binary_Search():
    
    for i in range(10):
        tab=[]
        s=randint(10,99)
        for i in range(s):
            tab.append(randint(0,999))
        tab=sorted(tab)
        index_in_random=randrange(0,s-1,1)
        Binary_return=BinarySearch(tab,tab[index_in_random])
        if Binary_return==index_in_random:
            print(tab)
            print(Binary_return,index_in_random)
            print("OK") 
To_Check_Binary_Search()    """         




""" for i in range(10):
    x= int (input())
    print(BinarySearch([0,1,2,3,4,5,6,7,8,9,10],x)) """

    

