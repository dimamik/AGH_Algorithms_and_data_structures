def Binary_Search_Recursive(tab, el_searching, start=0, end=-1):
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
for i in range(10):
    x= int (input())
    print(Binary_Search_Recursive([1,3,5,7],x))
print(Binary_Search_Recursive([1,2,3,7,9,15],15))