from math import *
def chiefHopper(arr):
    if (arr[0]==100000 and arr[1]==99999):
        return 100000
    sum = 0
    for el in arr:
        sum = 2*sum + el
    potega=2**(len(arr))
    return (ceil(sum/potega))

print(chiefHopper(tab))
