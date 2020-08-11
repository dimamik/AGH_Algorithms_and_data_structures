from zad3testy import runtests
""" Dzmitry Mikialevich """

""" 
Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
zawsze prawidłowa.)
 """
def Binary_Search_Recursive(tab, el_searching, start=0, end=-1):
    if (len(tab)==0):
        return -1
    """ 
    Zwraca -1 gdy nie ma elementu
    Lub jego index gdy jest
     """
    if end == -1:
        end = len(tab)
    if start >= end:
        """ 
    zamiast -1 return start or end
        """
        return -1 
    mid = (start+end)//2
    if tab[mid] == el_searching:
        return mid
    elif tab[mid] > el_searching:
        return Binary_Search_Recursive(tab, el_searching, start, mid)
    elif tab[mid] < el_searching:
        return Binary_Search_Recursive(tab, el_searching, mid+1, end)

def IncreaseCounter(A,tab_of_diff,tab_of_diff_count,k_th_max,k_th_current,i,j):
    """ 
    Returning k_th_current if is possible else -1
     """
    if (j+1<len(tab_of_diff)):
        index =Binary_Search_Recursive(tab_of_diff, A[j+1])
        if (index!=-1):
            if (tab_of_diff_count[index]==0):
                if (k_th_current+1 >= k_th_max):
                    return False
                else:
                    tab_of_diff_count[index]+=1
                    return k_th_current+1
            else:
                tab_of_diff_count[index]+=1
                return k_th_current

def DecreaseCounter(A,tab_of_diff,tab_of_diff_count,k_th_max,k_th_current,i,j):
    """ 
    Returning true or false depending on 
     """
    if (i+1<len(tab_of_diff)):
        index =Binary_Search_Recursive(tab_of_diff, A[i+1])
        if (index!=-1):
            tab_of_diff_count[index]-=1
            if (tab_of_diff_count[index]==0):
                return k_th_current-1
            else:
                return -1

def longest_incomplete( A, k ):
    """ Szukamy n różnych liczb """
    """ (Liczba,ilosc) """
    tab_of_diff =[]
    tab_of_diff_count = [0] * k
    print(tab_of_diff)
    for i in range(len(A)):
        index = Binary_Search_Recursive(tab_of_diff,A[i])
        if (index==-1):
            tab_of_diff.append(A[i])
            tab_of_diff.sort()
    print(tab_of_diff)
    """ Ręcznie dodaje pierwszy element """

    x = IncreaseCounter(A,tab_of_diff,tab_of_diff_count,k,1,0,0)
    y = DecreaseCounter(A,tab_of_diff,tab_of_diff_count,k,1,0,0)
    i=0
    j=0
    k_th_max = k
    k_th_current = 1
    max_len = 1
    index = Binary_Search_Recursive(tab_of_diff,A[0])
    tab_of_diff_count[index]+=1

    while (i<len(A) and j<len(A) and i<=j):
        if (k_th_current<k_th_max):

            """ !! """
            tmp = IncreaseCounter(A,tab_of_diff,tab_of_diff_count,k_th_max,k_th_current,i,j)
            
            k_th_current = tmp
            j+=1
        else:
            
            i+=1


    

A  = [1,2,3,1,2,3,1,2,3]
Ak = 3
Ar = 2

print(longest_incomplete(A,Ak))
