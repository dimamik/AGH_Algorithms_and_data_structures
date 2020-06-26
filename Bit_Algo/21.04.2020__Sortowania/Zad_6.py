def zad6(tab,l=0,r=-1):
    """  binary search """
    if r == -1:
        r = len(tab)
    if l >= r:
        return -1
    """ 
    zamiast -1 return l or r
     """
    mid = (l+r)//2
    if tab[mid] == mid:
        return 1
    elif tab[mid] > mid:
        return zad6(tab,  l, mid)
    elif tab[mid] < mid:
        return zad6(tab,  mid+1, r)
print(zad6([0.5,0.7,0.9,34]))
