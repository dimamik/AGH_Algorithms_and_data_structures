"""  Dany jest graf ważony, pozbawiony cyklów ujemnych. Podaj algorytm, który znajdzie 
najkrótsze ścieżki do wszystkich wierzchołków od źródła s, posiadające nie więcej niż k 
krawędzi. 
F(i,j) -> maxymalna dlugosc sciezki od zrodla s do wierzcholka i o dl j
"""
""" !!JEST BŁĘDNY!! """

""" HELPFULL STRUCTURES """
class Vertex():
    def __init__(self,id):
        """ 
        Inicialization is equivalent to operation make_set()
         """
        self.id=id
        self.parent_in_union=self
        self.rank_of_union=0
        self.parrent=-1
        self.color=-1
        self.tab_index_incident=[]
        self.visited=False
        self.entry=-1
        self.process=-1
        self.distance=0
    
class PseudoVertex():
    """ 
    Pomocnicza klasa dla przechowywania wag
     """
    def __init__(self,index=-1,waga=-1):
        self.index=index
        self.waga=waga
def BuildTab_of_v(tab,n,skierowany=False):
    """ 
    n - ilosc wierzcholkow (licząc od 0)
    [u,v,w] ->wierzcholek z u do v o wadze w
    takes tab=[[0,2,3],...[]]
     """
    tab_of_v=[None]*n
    for i in range(n):
        tab_of_v[i]=Vertex(i)
    for i in range(len(tab)):
        (tab_of_v[tab[i][0]].tab_index_incident).append(PseudoVertex(tab[i][1],tab[i][2])
        )
        if not skierowany:
            (tab_of_v[tab[i][1]].tab_index_incident).append(PseudoVertex(tab[i][0],tab[i][2])
        )
    return tab_of_v



def zad(tab_of_v,ilosc_krawedzi,s_index):
    """ Dynamic Programing """
    F = [None] * len(tab_of_v)
    for i in range(len(tab_of_v)):
        F[i]=[float("inf")]*2
    F[s_index][0]=0
    F[s_index][1]=0
    tab_of_v[s_index].distance=0
    """ for sasiedzi_u in tab_of_v[s_index].tab_index_incident:
        F[sasiedzi_u.index][1]=sasiedzi_u.waga """
    Q=[]
    count=0
    Q.append(s_index)
    """ To psuje rząd złożoności ale dalej działa xD """
    while len(Q)!=0:
        u=Q.pop()
        for v in tab_of_v[u].tab_index_incident:
            if F[v.index][1]>F[u][1]+1 or (F[v.index][1]==F[u][1] and F[v.index][0]>F[u][0]+v.waga):
                F[v.index][0]=F[u][0]+v.waga
                F[v.index][1]=F[u][1]+1
                count+=1
                Q.append(v.index)
                tab_of_v[v.index].distance+=1
                """ MORE FUNCTIONS LIKE PARRENT AND OTHERS """

    """ for i in range(len(tab_of_v)):
        print(tab_of_v[i].distance) """
    print(F)
    """ Zlozonosc wychodzi ?O(V^2E)? """
    pass


tab_v = BuildTab_of_v([[0,1,3],[1,5,2],[1,2,1],[2,3,1],[3,4,1],[5,4,1],[4,6,1]],7)
tab_v = BuildTab_of_v([[0,5,25],[5,4,50],[0,1,1],[1,2,1],[2,3,1],[3,4,1]],6)
zad(tab_v,6,0)
#zad(tab_v,7,0)