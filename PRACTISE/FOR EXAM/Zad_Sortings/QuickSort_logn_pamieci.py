""" 
Proszę zaimplementować algorytm QuickSort tak, żeby zużywał najwyżej
O(log n) pamięci (poza pamięcią na tablicę do posortowania),
niezleżnie od tego jakie podziały wskaże funkcja partition. Proszę
zwrócić uwagę, że jeśli funkcja partition będzie zawsze dzielić
tablicę wejściową (o rozmiarze n) na części o rozmiarze n-1 (mniejsze
lub równe pivotowi) i 1 (pivot) to standardowe implementacja
rekurencyjna zużyje O(n) pamięci na stosie. Należy tak pokierować
rekurencją, żeby zużyć najwyżej O(log n) pamięci.

Należy założyć, że dostępne są nastpujące operacje:

partition( A, i, j ) # wykonuje operację partition z QuickSorta na
obszarze tablicy od A[i] do A[j] (włącznie) i zwraca indeks k taki, że
elementy A[i], ..., A[k-1] mają wartości mniejsze lub równe A[k], a
elementy A[k+1], ..., A[j] (gdzie n to długość tablicy A) mają
wartości większe od A[k].


Funkcja powinna zaczynać się od:

def QuickSort( A, i, j ):      # posortuje fragment tablicy A[i], ..., A[j]
  ...
 """


def QuickSort( A, i, j ):
    while i<j:
        pivot=Lomuto_part(A,i,j)
        if pivot-i<j-pivot:
            QuickSort(A,i,pivot-1)
            i=pivot+1
        else:
            QuickSort(A,pivot+1,j)
            j=pivot-1

def Lomuto_part(tab,low,high):
    pivot = tab[high]
    curr_index=low-1
    for i in range(low,high):
        if tab[i]<=pivot:
            curr_index+=1
            tab[i],tab[curr_index]=tab[curr_index],tab[i]
    tab[curr_index+1],tab[high]=tab[high],tab[curr_index+1]
    return curr_index+1


n = 0


def q_sort(tab, low, high):
    global n
    n += 1
    """ if low < high:
        pivot_index = Lomuto_part(tab, low, high)
        q_sort(tab, low, pivot_index-1)
        q_sort(tab, pivot_index+1, high) """
    while low<high:
        pivot_index = Lomuto_part(tab, low, high)
        q_sort(tab,low,pivot_index-1)
        low=pivot_index+1

tab = [8, 4, 54, 54, 5, 4, 1, 18, 46, 4, 456, 2, 45, 4, 34, 6]

q_sort(tab, 0, len(tab)-1)
print(n)

def QuickSort_Iterative(tab):
    