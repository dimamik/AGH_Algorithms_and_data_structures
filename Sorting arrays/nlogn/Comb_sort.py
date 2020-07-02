""" !!UWAGA!! """


#Comb sort is improoved Bubble sort (with the help of lenght of swap >1)
#The gap starts with a large value and shrinks by a factor of 1.3 in every 
#iteration until it reaches the value 1. Thus Comb Sort removes 
#more than one inversion counts with one swap and performs better than Bublle Sort.
def get_next_gap(gap):  #Making the gap smaller (In worst cases degradate to Bubble Sort)
    gap=int ((gap*10)//13)
    if gap<1: return 1
    else:
        return gap
# Works faster even if we have only one presorted part of the array,
# But degradates when we have pre-sorted array 
def comb_sort(tab):
    n=len(tab)
    gap=n
    swapped=True    #Helps us to discard when having pre-sorted array
    while gap!=1 or swapped==1:
        gap=get_next_gap(gap)
        swapped=False
        for i in range(0,n-gap):    #To cover all array with gaps (..x...x...x...x...x..)
            if tab[i]>tab[i+gap]:   #Simply swapping if the elements d(x,y)=gap are not pre-sorted
                tab[i],tab[i+gap]=tab[i+gap],tab[i]
                swapped=True
    return tab

print(comb_sort([5,3,7,1,8,2]))

