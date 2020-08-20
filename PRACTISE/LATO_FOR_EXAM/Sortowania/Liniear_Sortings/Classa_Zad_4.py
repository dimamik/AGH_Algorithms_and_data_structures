""" 
Zaproponuj klasę reprezentującą strukturę danych, która w konstruktorze dostaje tablicę liczb naturalnych długości n o zakresie wartości [0, k]. Ma ona posiadać metodę count_num_in_range(a, b) - ma ona zwracać informację o tym, ile liczb w zakresie [a, b] było w tablicy, ma działać w czasie O(1). Można założyć, że zawsze a >= 1, b <= k.
 """


def CountintDiffSort(tab):
    max_el = max(tab)
    tab_c = [0] * (max_el+1)
    for i in range(len(tab)):
        tab_c[tab[i]] += 1
    for i in range(1, len(tab_c)):
        tab_c[i] += tab_c[i-1]
    return tab_c


class Zad4():
    def __init__(self, arr):
        self.arr = arr
        self.tab_c = CountintDiffSort(arr)

    def count_num_in_range(self, a, b):
        get_it = 0
        if (b == len(self.tab_c)-1):
            """ 
            Corner case with last value, two times being counted
             """
            get_it = -  (self.tab_c[a] - self.tab_c[a-1])
        return (self.tab_c[b]-self.tab_c[a]) + (self.tab_c[b]-self.tab_c[b-1]) + (self.tab_c[a] - self.tab_c[a-1]) + get_it


tab = [0, 5, 1, 9, 5, 3, 4, 1, 1, 5, 2, 3, 9, 9]
x = Zad4(tab)
print(x.count_num_in_range(1, 9))
