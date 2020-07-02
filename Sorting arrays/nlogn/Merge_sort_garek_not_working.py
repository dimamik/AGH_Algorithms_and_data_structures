""" NOT WORKING """




def merge(tab,p,sr,k):
    # Uwaga, sr is included in left_tab
    i=p
    j=sr+1
    tab_to_ret = [0] * (k-p+1)
    curr_index=0
    while i<=sr and j<=k:
        if tab[i]<=tab[j]:
            tab_to_ret[curr_index] = tab[i]
            curr_index+=1
            i+=1
        else:
            tab_to_ret[curr_index] = tab[j]
            curr_index+=1
            j+=1
    while i>sr and j<=k:
        tab_to_ret[curr_index] = tab[j]
        curr_index+=1
        j+=1
    while i<=sr and j>k:
        tab_to_ret[curr_index] = tab[i]
        curr_index+=1
        i+=1
    return tab_to_ret

def merge_sort(tab,p,k):
    if p!=k:
        sr=(p+k)//2
        merge_sort(tab,p,sr)
        merge_sort(tab,sr+1,k)
        tab = merge(tab,p,sr,k)
    return tab


print(merge_sort([1,3,1,7,2,4,6,8],0,7))
        




