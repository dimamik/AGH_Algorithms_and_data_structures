def Lomuto_part(tab,low,high):
    pivot = tab[high]
    curr_index=low-1
    for i in range(low,high):
        if tab[i]<=pivot:
            curr_index+=1
            tab[i],tab[curr_index]=tab[curr_index],tab[i]
    tab[curr_index+1],tab[high]=tab[high],tab[curr_index+1]
    return curr_index+1

def kthSmallest(tab,k,l,r): 
    """ 
    Dziala rekursywnie wiec nie da sie zamienic l i r
     """
    if (k > 0 and k <= r - l + 1): 
  

        index = Lomuto_part(tab, l, r) 

        if (index - l == k - 1): 
            return tab[index] 

        if (index - l > k - 1): 
            return kthSmallest(tab, l, index - 1, k) 
 
        return kthSmallest(tab, index + 1, r,  
                            k - index + l - 1) 
    return float("inf") 

print(kthSmallest([2,5,1,8,3,6],0,5,3))
