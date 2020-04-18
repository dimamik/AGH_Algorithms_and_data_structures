def Counting_sort(tab,decimal):#Decimal is 10/100/1000 etc.
    #So we are working with the numbers we use 0-9 notation
    
    tab_c=[0]*10
    tab_to_return=[0]*len(tab)
    for i in range(len(tab)):
        number=tab[i]//(decimal//10)
        number%=10
        tab_c[number]+=1
    for i in range(1,len(tab_c)):
        tab_c[i]+=tab_c[i-1]
    for i in range(len(tab)-1,-1,-1):
        number=tab[i]//(decimal//10)
        number%=10
        index=tab_c[number]-1
        tab_to_return[index]=tab[i]
        tab_c[number]-=1
    return tab_to_return

def Radix_sort(tab):
    #Finding max_decimal
    max_el=tab[0]
    for i in range(len(tab)):
        max_el=max(max_el,tab[i])
    max_decimal=1
    while max_el>0:
        max_el/=10
        max_decimal*=10
    tmp_decimal=10
    while tmp_decimal<=max_decimal:
        tab=Counting_sort(tab,tmp_decimal)
        tmp_decimal*=10
    return tab

print(Radix_sort([0,15,14,123,123,121,120,128]))
