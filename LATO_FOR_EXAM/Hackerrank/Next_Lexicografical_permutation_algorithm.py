def Next_Permutation_Algorithm(tab):
    """ 
    Takes a tab of ints each int is from 0 to 9 and then returns next permutation as following:
    https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
     """
    
    """ Finding suffix """
    for i in range(len(tab)-1,-1,-1):
        if (i==0 or tab[i-1]<tab[i]):
            break
    """ i is the last element of a suffix, so the pivot is on i-1"""
    if (i-1==-1):
        
        return -1
    pivot = tab[i-1]
    pivot_index = i-1
    """ Finding rightmost successor to pivot """
    pivot_successor_index = -1
    for j in range(len(tab)-1,0,-1):
        if (tab[j]>pivot):
            pivot_successor_index = j
            pivot_successor =tab[j]
            break
    tab[pivot_index],tab[pivot_successor_index] = tab[pivot_successor_index], tab[pivot_index]

    """ Reversing the suffix """
    end = len(tab)-1
    beg = pivot_index+1
    while (beg<end):
        tab[beg],tab[end] = tab[end],tab[beg]
        beg+=1
        end-=1
    return tab

""" print(Next_Permutation_Algorithm([0,1,2,5,3,3,0])) """
x = [0,1,2,3]
print(x)
x = Next_Permutation_Algorithm(x)
c=1
while (x!=-1):
    print(x)
    x = Next_Permutation_Algorithm(x)
    c+=1
print(c)

    