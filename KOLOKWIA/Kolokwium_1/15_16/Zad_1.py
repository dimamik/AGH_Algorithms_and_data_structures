""" 
SumSort

 """

def SumSort(tab,n):
    tab_of_Sums=[0]*n
    tab_of_first_ind=[0]*n
    tab_of_last_next_ind=[0]*n
    ind_filling=0
    curr_sum=0
    are_Filling_First=True
    for i in range((n*n)+1):
        if i%n==0 and i!=0:
            tab_of_Sums[ind_filling]=curr_sum
            tab_of_last_next_ind[ind_filling]=i
            ind_filling+=1
            
            are_Filling_First=True
            if i!=(n*n): 
                tab_of_first_ind[ind_filling]=i
                curr_sum=tab[i]
        else:
            if i!=(n*n): curr_sum+=tab[i]
    #Now connect the sum and the indexes and sort by sum
    connected_tab=[None]*n
    for i in range(n):
        connected_tab[i]=[0]*3
    for i in range(n):
        connected_tab[i][0]=tab_of_Sums[i]
        connected_tab[i][1]=tab_of_first_ind[i]
        connected_tab[i][2]=tab_of_last_next_ind[i]
    print(connected_tab)
    connected_tab=sorted(connected_tab)
    to_return=[0]*(n*n)
    index_in_tab_to_return=0
    for i in range(n):
        first=connected_tab[i][1]
        end=connected_tab[i][2]
        for i in range(first,end):
            to_return[index_in_tab_to_return]=tab[i]
            index_in_tab_to_return+=1
    
    return to_return

print(SumSort([9,8,7,6,5,4,3,2,1],3))