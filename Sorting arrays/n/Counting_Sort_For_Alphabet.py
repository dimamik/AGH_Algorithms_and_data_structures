def CountingSort(tab,pozition):
    """ 
    Counting sort for string via alphabetic liters
    and same lenghth all
     """
    tab_of_liters=[0]*(32)
    for i in range(len(tab)):
        index=ord(tab[i][pozition])-97
        tab_of_liters[index]+=1
    for i in range(1,len(tab_of_liters)):
        tab_of_liters[i]+=tab_of_liters[i-1]
    tab_to_return = [None]*len(tab)
    for i in range(len(tab)-1,-1,-1):
        index_in_ret = tab_of_liters[ord(tab[i][pozition])-97]-1
        tab_to_return[index_in_ret]=tab[i]
        tab_of_liters[ord(tab[i][pozition])-97]-=1
    return tab_to_return

""" 
def RadixSort(tab,n):
    for i in range(n,-1,-1):
        tab=CountingSort(tab,i)
    return tab
def SortString(tab):
    max_len=float("-inf")
    for i in range(len(tab)):
        max_len=max(max_len,len(tab[i]))
    Buckets=[[] for _ in range(max_len+1)]
    for i in range(len(tab)):
        Buckets[len(tab[i])].append(tab[i])
    for i in range(len(Buckets)):
        Buckets[i]=RadixSort(Buckets[i],i-1)
    #Connect buckets
    to_return=[None]*len(tab)
    index_in_ret=0
    for i in range(len(Buckets)):
        for k in range(len(Buckets[i])):
            to_return[index_in_ret]=(Buckets[i][k])
            index_in_ret+=1
    return to_return

print(SortString(["asjkda","ajs","a","aa","abcd"])) """