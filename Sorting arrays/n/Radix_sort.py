def Counting_sort(tab, decimal):  
    """ 
    Decimal is 10/100/1000 etc.
    So we are working with the numbers we use 0-9 notation 
    """
    tab_c = [0]*10
    tab_to_return = [0]*len(tab)
    for i in range(len(tab)):
        number = tab[i]//(decimal//10)
        number %= 10
        tab_c[number] += 1
    for i in range(1, len(tab_c)):
        tab_c[i] += tab_c[i-1]
    for i in range(len(tab)-1, -1, -1):
        number = tab[i]//(decimal//10)
        number %= 10
        index = tab_c[number]-1
        tab_to_return[index] = tab[i]
        tab_c[number] -= 1
    return tab_to_return


def Radix_sort(tab):
    """ 
    Stabliny -> O(d * (n+k)) , d - max ilosc pozycji , n - len(tab) , k - maksymalna cyfra (w systemie dziesietnym -> 9)
    Najlepiej się stosuje na tej samej długośći danych
    Polega na przejsciu od ostatniego znaku do poczatku i stosowanie stablinego algorytmu sortowania dla tego znaku i tych danych
     """
    #Finding max element to find max decimal
    max_el = tab[0]
    for i in range(len(tab)):
        max_el = max(max_el, tab[i])
    #Finding max_decimal
    max_decimal = 1
    while max_el > 1:
        max_el /= 10
        max_decimal *= 10
    tmp_decimal = 10
    while tmp_decimal <= max_decimal:
        """ 
        Bo dziele przez tą wartość
         """
        tab = Counting_sort(tab, tmp_decimal)
        tmp_decimal *= 10
    return tab


print(Radix_sort([0, 156748, 15, 14, 123, 123, 121, 120, 128, 1564897]))




""" TESTING """
from random import *
import time
def Timer(func):
    def wrapper(*args,**kwargs):
        tic = time.perf_counter()
        output=func(*args,**kwargs)
        toc = time.perf_counter()
        print(toc)
        return output
    return wrapper
@Timer
def Checker(SortingFunc,k=150):
    positive=0
    all=k
    for i in range(k):
        tab=[]
        s=randint(10,999)
        for i in range(s):
            tab.append(randint(0,999))
        return_from_funct=SortingFunc(tab)
        if return_from_funct==sorted(tab):
            print("Test passed")
            positive+=1
        else:
            """ print(return_from_funct,sorted(tab)) """
            print("Test Failed")
    print("ALL TESTS PASSED WITH A SCORE", positive,"/",all)

# Checker(Radix_sort,1000)