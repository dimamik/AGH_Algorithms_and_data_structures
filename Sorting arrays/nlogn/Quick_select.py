def Lomuto_part(tab,low,high):
    pivot = tab[high]
    curr_index=low-1
    for i in range(low,high):
        if tab[i]<=pivot:
            curr_index+=1
            tab[i],tab[curr_index]=tab[curr_index],tab[i]
    tab[curr_index+1],tab[high]=tab[high],tab[curr_index+1]
    return curr_index+1

def kthSmallest(arr, l, r, k): 
  
    # if k is smaller than number of 
    # elements in array 
    if (k > 0 and k <= r - l + 1): 
  
        # Partition the array around last 
        # element and get position of pivot 
        # element in sorted array 
        index = Lomuto_part(arr, l, r) 
  
        # if position is same as k 
        if (index - l == k - 1): 
            return arr[index] 
  
        # If position is more, recur  
        # for left subarray  
        if (index - l > k - 1): 
            return kthSmallest(arr, l, index - 1, k) 
  
        # Else recur for right subarray  
        return kthSmallest(arr, index + 1, r,  
                            k - index + l - 1) 
    return float("inf")

print(kthSmallest([2,5,1,8,3,6],0,5,3))
