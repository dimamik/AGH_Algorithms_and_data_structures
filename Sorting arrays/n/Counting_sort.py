def Counting_sort(tab):
    """ 
    Stabliny -> O(n+k), n - len(tab) , k - wartośći
    Najlepiej działa dla zakresu liczb [0,k] i k<<n
     """
    #Finding max element to define the range
    max_el = tab[0]
    for i in range(len(tab)):
        if tab[i] > max_el:
            max_el = tab[i]
    tab_c = [0]*(max_el+1)
    for i in tab:
        tab_c[i] += 1
    for i in range(1, len(tab_c)):
        tab_c[i] += tab_c[i-1]
    tab_to_return = [0]*len(tab)
    for i in range(len(tab)-1, -1, -1):
        index_in_ret = tab_c[tab[i]]-1
        tab_to_return[index_in_ret] = tab[i]
        tab_c[tab[i]] -= 1
    return tab_to_return


print(Counting_sort([1, 2, 2, 5, 1, 2, 0, 9, 3]))

