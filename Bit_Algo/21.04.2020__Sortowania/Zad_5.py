def BiSearch(tab, el_searching, start=0, end=-1):
    if end == -1:
        end = len(tab)
    if start >= end:
        return -1
    mid = (start+end)//2
    if tab[mid] == el_searching:
        return mid
    if mid==0:
        return -1
    elif tab[mid]==None or tab[mid] > el_searching:
        return BiSearch(tab, el_searching, start, mid)
    elif tab[mid] < el_searching:
        return BiSearch(tab, el_searching, mid+1, end)    


from random import *
def zad6(tab,x):
    last=-1
    i=1
    while i<len(tab) and tab[i]!=None:
        i=2*i
        """ print(i,end='') """
    last=min(i,len(tab))
    """ Binary search with respect to None """
    output=BiSearch(tab,x,0,last)
    if output==-1:
        """ print("NO") """
        return -1
    else:
        """ print(output) """
        return output

def Checker(zad6,x=10):
    """ 
    Generating random tab
     """
    rate=0
    for i in range(x):
        dl=randint(0,999)
        dl_None=randint(0,999)
        tab=[]
        for i in range(dl):
            tab.append(randint(-500,999))
        tab=sorted(tab)
        for i in range(dl_None):
            tab.append(None)
        rand_index=randint(0,dl)
        f=randint(0,999)
        k=choice([tab[rand_index],f])
        zad=zad6(tab,k)
        if zad==rand_index or (k==f and zad==-1) or (tab[zad]==k):
            print("OK")
            rate+=1
        else:
            raise "Blad"
            print("BLAD")

        """ print(tab) """
    print(rate,"/",x)



Checker(zad6)
""" print(zad6([1,3,7,9,15,156,None,None,None,None,None,None,None,None],156))
 """

    