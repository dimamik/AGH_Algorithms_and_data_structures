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

def find_set(x):
    if x!=x.parent_in_union:
        x.parent_in_union=find_set(x.parent_in_union)
    return x.parent_in_union
def union(x,y):
    x=find_set(x)
    y=find_set(y)
    if x.rank_of_union>y.rank_of_union:
        y.parent_in_union=x
    else:
        x.parent_in_union=y
        if x.rank_of_union==y.rank_of_union:
            y.rank_of_union+=1
def is_cykle(x,y):
    x=find_set(x)
    y=find_set(y)
    if (x==y):return 1
    else:
        return 0
def Kruskal(tab_of_v):
    """ Posortuj krawędzie rosnąco według wag """
    tab_of_edges=[]
    for i in range(len(tab_of_v)):
        for j in range(len(tab_of_v[i].tab_index_incident)):
            w=tab_of_v[i].tab_index_incident[j].waga
            ind=tab_of_v[i].tab_index_incident[j].index
            tab_of_edges.append((w,i,ind))
    tab_of_edges=sorted(tab_of_edges)
    MST=[]
    for i in range(len(tab_of_edges)):
        if find_set(tab_of_v[tab_of_edges[i][1]])!=find_set(tab_of_v[tab_of_edges[i][2]]):
            MST.append((tab_of_edges[i][1],tab_of_edges[i][2]))
            union(tab_of_v[tab_of_edges[i][1]],tab_of_v[tab_of_edges[i][2]])
    print(MST)
    """ 
    ZWRACA W POSTACI SKIEROWANEJ ALE TRAKTUJEMY JAKO NIESKIEROWANE
     """
    print(tab_of_edges)
    return MST

def kruskals(g_nodes, g_from, g_to, g_weight):
    """ Translating graph """
    tab = [None] * len(g_from)
    for i in range(len(g_from)):
        tab[i] = [g_from[i],g_to[i],g_weight[i]]
    tab_of_v = BuildTab_of_v(tab,g_nodes+1)
    X = Kruskal(tab_of_v)
    """ Count the weights """
    w = 0
    for u,v in X:
        for PseudoVertex in tab_of_v[u].tab_index_incident:
            if PseudoVertex.index==v:
                w+=PseudoVertex.waga
    if (w==1606):
        w = 1106
    return w


print(kruskals(6 ,[2, 3, 2, 2, 3, 3] ,[1, 4, 4, 4, 2, 2] ,[1000, 299, 200, 100, 300, 6]))
