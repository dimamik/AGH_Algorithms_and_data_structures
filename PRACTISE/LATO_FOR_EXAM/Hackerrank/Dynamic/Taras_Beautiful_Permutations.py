from math import *
def n_po_k(n,repeats):
    """ 
    Repeats is the number of repeats of each group
     """
    return factorial(n)/sum(map(factorial,repeats))

def beautifulPermutations(arr):
    arr_set = dict.fromkeys(set(arr),0)
    for el in arr:
        arr_set[el]+=1
    sum_el = len(arr)
    val_povt = list(arr_set.values())
    all_perm = n_po_k(sum_el,val_povt)
    to_subst = 0
    to_subst = n_po_k(len(val_povt))
    pass
print(beautifulPermutations([1, 2, 2, 1]))
