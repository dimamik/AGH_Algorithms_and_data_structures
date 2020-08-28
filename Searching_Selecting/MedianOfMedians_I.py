def MedianOfMedians(L, j):
    """ 
    Works in O(n) in all cases (Magiczne Piątki)
     """
    if len(L) < 10:
        L.sort()
        return L[j]
    S = []
    lIndex = 0
    while lIndex+5 < len(L)-1:
        S.append(L[lIndex:lIndex+5])
        lIndex += 5
    S.append(L[lIndex:])
    Meds = []
    for subList in S:
        Meds.append(MedianOfMedians(subList, int((len(subList)-1)/2)))
    med = MedianOfMedians(Meds, int((len(Meds)-1)/2))
    L1 = []
    L2 = []
    L3 = []
    for i in L:
        if i < med:
            L1.append(i)
        elif i > med:
            L3.append(i)
        else:
            L2.append(i)
    if j < len(L1):
        return MedianOfMedians(L1, j)
    elif j < len(L2) + len(L1):
        return L2[0]
    else:
        return MedianOfMedians(L3, j-len(L1)-len(L2))
print(MedianOfMedians([8,7,6,5,4,3],2))