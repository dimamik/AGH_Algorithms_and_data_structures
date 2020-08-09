""" 
https://www.hackerrank.com/challenges/lilys-homework/problem

Return the minimum number of swaps needed to make the array beautifulw (sorted).

So the problem is to count swaps in sorted array from unsorted
 """

def Binary_Search_Recursive(tab, el_searching, start=0, end=-1):
    if end == -1:
        end = len(tab)
    if start >= end:
        return -1

    mid = (start+end)//2
    if tab[mid] == el_searching:
        return mid

    elif tab[mid] > el_searching:
        return Binary_Search_Recursive(tab, el_searching, start, mid)
    elif tab[mid] < el_searching:
        return Binary_Search_Recursive(tab, el_searching, mid+1, end)


def Zad_1(tab):
    tab_tmp = [0] * len(tab)
    for i in range(len(tab)):
       tab_tmp[i]= tab[i]
    tab_sorted = sorted(tab)
    swaps=0
    for i in range(len(tab)):
        index = Binary_Search_Recursive(tab_sorted,tab[i])
        if (index != i):
            tab[i],tab[index] = tab[index],tab[i]
            swaps+=1
    for i in range(len(tab)):
        tab[i]=tab_tmp[i]
    return swaps


def Zad_1a(tab):
    tab_sorted = sorted(tab)
    swaps=0
    for i in range(len(tab)):
        index = Binary_Search_Recursive(tab_sorted,tab[i])
        index = abs(len(tab)-1-index)
        if (index != i):
            tab[i],tab[index] = tab[index],tab[i]
            swaps+=1
    return swaps

def lilysHomework(arr):
    return min(Zad_1(arr),Zad_1a(arr))

print(lilysHomework( [] ))
