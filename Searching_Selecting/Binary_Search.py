def Binary_Search(tab,el_searching,start=0,end=-1):
    """ 
    Returning -1 if there is no such an element,
    and if there is than returning el_index
     """
    if end==-1: end=len(tab)
    if start>=end : return -1
    """ 
    zamiast -1 return start or end
     """
    mid=(start+end)//2
    if tab[mid]==el_searching:return mid
    if mid==0: return -1
    elif tab[mid]>el_searching: return Binary_Search(tab,el_searching,start,mid)
    elif tab[mid]<el_searching: return Binary_Search(tab,el_searching,mid+1,end)

print(Binary_Search([1,2,3,7,9,15],8))

