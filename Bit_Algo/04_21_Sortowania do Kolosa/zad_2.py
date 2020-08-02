def Binary_Search_Recursive(tab, el_searching, start=0, end=-1):
    """ 
    Zwraca -1 gdy nie ma elementu
    Lub jego index gdy jest
     """
    if end == -1:
        end = len(tab)
    if start >= end:
        return -1
    """ 
    zamiast -1 return start or end
     """
    mid = (start+end)//2
    if tab[mid] == el_searching:
        return mid
    if mid == 0:
        return -1
    elif tab[mid] > el_searching:
        return Binary_Search_Recursive(tab, el_searching, start, mid)
    elif tab[mid] < el_searching:
        return Binary_Search_Recursive(tab, el_searching, mid+1, end)

def zad_2(m,n):
    m=sorted(m)
    for i in range(len(n)):
        if Binary_Search_Recursive(m,n[i])!=-1:
            return "Nie"
    return "Tak, rozłączne"

print(zad_2([9,0,6],[1,2,0,3,4,5,456]))