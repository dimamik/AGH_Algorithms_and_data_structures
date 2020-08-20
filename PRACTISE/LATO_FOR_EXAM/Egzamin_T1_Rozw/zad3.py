from zad3testy import runtests
import math
""" Dzmitry Mikialevich """

""" 
Bucket sort stosowany do liczb x w a, bo wiemy ze rozklad jest rownomierny i wiemy, ze przedzial to [0,1]
 """


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
    if high==-1:
        high=len(tab)-1
    if low<high:
        piv_idex=Hoare_part(tab,low,high)
        Quick_Sort(tab,low,piv_idex)
        Quick_Sort(tab,piv_idex+1,high)
    return tab
                 
    
def fast_sort(tab, a):
    for i in  range(len(tab)):
        tab[i] = [math.log(tab[i],a),tab[i]]
    
    """ Bucket Sort """
    max_el = 0
    for i in range(len(tab)):
        max_el = max(max_el,tab[i][0])
    n=len(tab)
    
    rozd_Bucketa=max_el/len(tab)
    Buckets=[[] for _ in range(n+1)]
    for number in tab:
        index_of_Bucket=int (number[0]/rozd_Bucketa)
        #add using insertion sort in bucket (but in this case just add)
        Buckets[index_of_Bucket].append(number)
    for i in range(n+1):
        Buckets[i]=Quick_Sort(Buckets[i])
    to_return=[]
    for i in range(n+1):
        for j in range(len(Buckets[i])):
            to_return.append(Buckets[i][j][1])
    return to_return



runtests( fast_sort )
