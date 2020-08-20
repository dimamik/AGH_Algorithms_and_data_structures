""" 
Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który posortuje tę tablicę w czasie O(n).
Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.

SORTED:= aaa>aaaa and aaaaa>aaaab and bb > aaa (Czyli najpierw po dlugosci potem po alfabetu)
 """

def CountingSortForChar(tab, num_of_char_from_begining):
    """ 
    Counting Sort With a Small Alphabet Letters
     """
    alphabet = [0] * 26
    for i in range(len(tab)):
        index = ord(tab[i][1][num_of_char_from_begining-1]) - 97
        alphabet[index] += 1
    for i in range(len(alphabet)-1):
        alphabet[i+1] += alphabet[i]
    tab_to_ret = [None] * len(tab)
    for i in range(len(tab)-1, -1, -1):
        """ Get the index of letter """
        index_in_alphabet = ord(tab[i][1][num_of_char_from_begining-1]) - 97
        tab_to_ret[alphabet[index_in_alphabet] - 1] = tab[i]
        alphabet[index_in_alphabet] -= 1
    for i in range(len(tab)):
        tab[i] = tab_to_ret[i]


""" print(CountingSortForChar([(3,"aab"),(3,"aaa"),(3,"aac"),(3,"aaa")],3)) """


def RadixSortForStringsOfSameLenght(tab):
    """ 
    tab - tablica krotek (len,string)
    Algorytm polega na przejsciu od konca do poczatku i stosowanie Counting_Sorta
     """
    for i in range(len(tab)-1, -1, -1):
        """ Tu juz mamy litere """
        CountingSortForChar(tab, i)
    return tab


def BucketSortForLenghth(tab):
    """ 
    UWAGA NA TO, ŻE SORTUJEMY PO DLUGOSCI A POTEM LEKSYKOGRAFICZNIE
     """

    for i in range(len(tab)):
        tab[i] = (len(tab[i]), tab[i])

    """ Bucket Sort, because len is [0,n] """

    max_el = max(tab)
    max_el = max_el[0]
    n = len(tab)
    rozd_Bucketa = max_el/len(tab)
    Buckets = [[] for _ in range(n+1)]
    for number in tab:
        index_of_Bucket = int(number[0]/rozd_Bucketa)
        #add using insertion sort in bucket (but in this case just add)
        Buckets[index_of_Bucket].append(number)
    for i in range(n+1):
        """ 
        Radix Sort for alphabet numbers
         """
        RadixSortForStringsOfSameLenght(Buckets[i])
    to_return = []
    for i in range(n+1):
        for j in range(len(Buckets[i])):
            to_return.append(Buckets[i][j][1])
    return to_return

tab = ["aaa",  "bb", "aaab", "aaaa", "b", "asdkadsa"]
BucketSortForLenghth(tab)

