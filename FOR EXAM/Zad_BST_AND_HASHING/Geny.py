""" 
W pewnym laboratorium genetycznym
powstał ciąg sekwencji DNA. Każda sekwencja to pewien napis składający się z symboli G, A, T , i C. Przed
dalszymi badaniami konieczne jest upewnić się, że wszystkie sekwencje DNA są parami rózne. Proszę opisać
algorytm, który sprawdza czy tak faktycznie jest.
 """
class Node():
    """ 
    G A T C
     """
    def __init__(self,literka=None):
        self.literka=literka
        self.tab_dzieci=[None]*6
def Litera_to_num(litera):
    switcher = {
        "G": 0,
        "A": 1,
        "T": 2,
        "C": 3,
        "X": 4,
        "E":5
    }
    return switcher.get(litera,"EROR")

""" print(Litera_to_num("G")) """

def zad(tab):
    r=Node("X")
    tmp=r
    for i in range(len(tab)):
        nr_litery=0
        tmp=r
        for litera in tab[i][0]:
            if tmp.tab_dzieci[Litera_to_num(litera)]==None:
                X=Node(litera)
                tmp.tab_dzieci[Litera_to_num(litera)]=X
                tmp=X
            else:
                tmp=tmp.tab_dzieci[Litera_to_num(litera)]
            nr_litery+=1
            if nr_litery==len(tab[i][0]) and tmp.tab_dzieci[Litera_to_num("E")]!=None:
                return "Nie są parami rózne"
        tmp.tab_dzieci[Litera_to_num("E")]=1
            
    return "Są parami różne"

print(zad([["A"],["AT"],["TCAG"]]))

