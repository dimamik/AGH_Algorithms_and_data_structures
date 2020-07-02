""" NOT WORKING """

""" Dany graf ważony z małymi naturalnymi wagami, znaleźć najkrótszą ścieżkę z u do v """

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
from queue import *
def BFSNaWazonych(tab_of_v,s_ind,t_ind):
    Q=Queue()
    tab_of_v[s_ind].distance=0
    tab_of_v[s_ind].visited=True
    tab_of_v[s_ind].parrent=None
    s=PseudoVertex(s_ind,1)
    Q.put(s)
    while not Q.empty():
        u_class=Q.get()
        u_ind=u_class.index
        #print (list(Q.queue))
        for v_pseudo in tab_of_v[u_ind].tab_index_incident:
            v_ind=v_pseudo.index
            if v_pseudo.waga>1:
                v_pseudo.waga-=1
                tab_of_v[v_ind].distance=tab_of_v[u_ind].distance+1
                Q.put(u_class)
                continue
            if not tab_of_v[v_ind].visited:
                if v_ind==t_ind:
                    return u_ind
                tab_of_v[v_ind].visited=True
                tab_of_v[v_ind].distance=tab_of_v[u_ind].distance+1
                tab_of_v[v_ind].parrent=u_ind
                Q.put(PseudoVertex(v_ind,v_pseudo.waga))
    for i in range(len(tab_of_v)):
        #print(tab_of_v[i].distance)
        print(tab_of_v[i].parrent)

tab_v = BuildTab_of_v([[1,3,10],[1,2,2],[2,4,3],[4,5,1],[1,5,20],[3,5,2]],6,True)
print(BFSNaWazonych(tab_v,1,5))

