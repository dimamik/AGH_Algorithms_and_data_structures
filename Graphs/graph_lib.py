
""" 
Reprezentacja poprzez listy sąsiedstwa
Implementacja poprzez tablice połączeń danego wierzchołku
Np: [[1,2],[0],[0]] 
 """
class Vertex():
    def __init__(self):
        self.visited=False
        self.parrent=None
        self.index=0
        self.waga=0
        self.distance=float("inf")
        self.d=0


def Polacz_Wierzch_ls(tab,index_wierz):
    return tab[index_wierz]
def Are_Connnected_in_directed_ls(tab,fw,sw):
    if sw in tab[fw]:
        return 1
    return 0
def Input_ls_Graph():
    V,E=map(int,input().strip().split())
    tab= [None] * (V+1)
    for i in range(E):
        vert_tmp = Vertex()
        x,y,w=map(int,input().strip().split())
        vert_tmp.index=y
        vert_tmp.waga=w
        tab[x]=vert_tmp
    print(tab)



""" 
Reprezentacja poprzez Macierz sąsiedstwa

     0 1 2 3
   0   x 
   1 x   x x
   2   x   x
   3   x x
 """
def Polacz_Wierzch_ms(tab,index_wierz):
    tab_of_wierz=[]
    for i in range(len(tab)):
        if tab[index_wierz][i]!=0:
            tab_of_wierz.append(i)
    return tab_of_wierz
def Are_Connnected_in_directed_ms(tab,fw,sw):
    if fw>=len(tab) or sw>=len(tab):
        return 0
    return tab[fw][sw]!=0
def Input_MSGraph():
    n=int (input())
    tab=[0]*n
    for i in range(len(tab)):
        tab[i]=[0]*n
    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j]=int (input())
    return tab

    
    