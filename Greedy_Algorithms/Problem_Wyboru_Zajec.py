""" 
Wybrac jak najliczniejszy zbior zajec majac tab  = [[0,1],[1,2],...] tablice poczatku i koncu zajec
 """

def WyborZajec(tab):
    """ 
    Biore zawsze najwczesniej konczacy sie element
    O( nlogn  + n )
     """
    tab = sorted(tab,key=lambda x: x[1])
    i=1
    last_end = tab[0][1]
    last_beg = tab[0][0]
    to_ret = []
    to_ret.append(tab[0])
    while i<len(tab):
        if (last_end > tab[i][0]):
            i+=1
        else:
            to_ret.append(tab[i])
            last_end = tab[i][1]
            last_beg = tab[i][0]
            i+=1
    return to_ret

WyborZajec([[1,6],[8,11],[5,7],[0,3],[10,12],[2,9],[3,8],[3,5]])