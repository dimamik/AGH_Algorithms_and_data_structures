#Lomuto_part dziala jak insertion sort dla pivota
def Lomuto_part(tab,low,high):
    pivot = tab[high]
    curr_index=low-1
    for i in range(low,high):
        if tab[i]<=pivot:
            curr_index+=1
            tab[i],tab[curr_index]=tab[curr_index],tab[i]
    tab[curr_index+1],tab[high]=tab[high],tab[curr_index+1]
    return curr_index+1
def q_sort(tab,low=0,high=-1):
    if high==-1:
        high=len(tab)-1
    if low<high:
        pivot_index=Lomuto_part(tab,low,high)
        q_sort(tab,low,pivot_index-1)
        q_sort(tab,pivot_index+1,high)
    return tab

tab=[3,2,1,0,1,2,5,6,7,3]
print(q_sort(tab))
    



