""" 
A vertex in an undirected connected graph is an articulation point (or cut vertex) iff removing it (and edges through it) disconnects the graph. Articulation points represent vulnerabilities in a connected network – single points whose failure would split the network into 2 or more components. They are useful for designing reliable networks.
 """
""" HELPFULL STRUCTURES """
class Vertex():
    """ 
    The way of using:
    [x,y,z], x-veris
     """
    def __init__(self):
        self.parrent=-1
        self.color=-1
        self.tab_index_incident=[]
        self.visited=False
        self.entry=float("inf")
        self.process=-1
        self.wsteczna=-1
        self.low=float("inf")
def BuildFromInc(tab):
    """ 
    Buduje z listy sąsiedstwa w postaci tablicy
    Lista sąsiedstwa tab
    tab=[[2,3],[1,5],...]
     """
    tab_of_v=[None]*len(tab)
    for i in range(len(tab)):
        V=Vertex()
        V.tab_index_incident=tab[i]
        tab_of_v[i]=V
    return tab_of_v

""" MOSTY W GRAFIE NIESKIEROWANYM"""



""" DFS Pomocniczy """
time=0
def DFS_Usual_Visit_Parent_and_Wsteczne(u_index,tab_of_v,tab_art):
    """ 
    DFS, zwraca tablicę krawędzi wstecznych,parrent i td
     """
    global time
    tab_of_v[u_index].visited=True
    tab_of_v[u_index].entry=time
    tab_of_v[u_index].low=time
    time+=1
    children=0
    for v_ind in tab_of_v[u_index].tab_index_incident:
        if not tab_of_v[v_ind].visited:
            tab_of_v[v_ind].parrent=u_index
            children+=1
            DFS_Usual_Visit_Parent_and_Wsteczne(v_ind,tab_of_v,tab_art)  
            tab_of_v[u_index].low=min(tab_of_v[v_ind].low,tab_of_v[u_index].low)
            if tab_of_v[u_index].parrent==-1 and children>1:
                tab_art[u_index]=1
            if tab_of_v[u_index].parrent!=-1 and tab_of_v[v_ind].low>=tab_of_v[u_index].entry:
                tab_art[u_index]=1  
        else:
            if tab_of_v[u_index].parrent!=v_ind:
                """ Krawędź wsteczna tu jest, bo już odwiedzony i nie rodzic"""
                tab_of_v[u_index].low=min(tab_of_v[u_index].low,tab_of_v[v_ind].entry)
                tab_of_v[u_index].wsteczna=v_ind

    """ time+=1
    tab_of_v[u_index].process=time """

def DFS_Parent_and_Wsteczne(tab_of_v):
    tab_art=[0]*len(tab_of_v)
    tab_of_korzen=[]
    for v_ind in range(len(tab_of_v)):
        if not tab_of_v[v_ind].visited:
            DFS_Usual_Visit_Parent_and_Wsteczne(v_ind,tab_of_v,tab_art)
            """ In this moment I have A DFS tree """
    """ Writing out the parrents tab """
    tab_p=[0]*len(tab_of_v)
    tab_w=[0]*len(tab_of_v)
    tab_l=[0]*len(tab_of_v)
    tab_time=[0]*len(tab_of_v)
    for  i in range(len(tab_of_v)):
        tab_p[i]=tab_of_v[i].parrent
        tab_w[i]=tab_of_v[i].wsteczna
        tab_l[i]=tab_of_v[i].low
        tab_time[i]=tab_of_v[i].entry
    return tab_of_korzen,tab_art,tab_time,tab_p,tab_w,tab_l

def PunktyArtykulacji(tab_of_v):
    """ 
    Returns: tablice punktow artykulacji grafu w postaci listy sasiedstwa G=[[...]]
    
     """
    tab_of_korzen,tab_art,tab_entry,tab_p,tab_w,tab_l=DFS_Parent_and_Wsteczne(tab_of_v)    
    for i in range(len(tab_of_v)):
        tab_l[i]=tab_of_v[i].low
    for i in range(len(tab_p)):
        if tab_p[i]!=-1 and tab_of_v[i].low>=tab_of_v[tab_p[i]].entry:
            for el in tab_of_korzen:
                if el!=tab_p[i]:
                    tab_art.append(tab_p[i])
    art_points=[]
    for i in range(len(tab_art)):
        if tab_art[i]==1:
            art_points.append(i)
    return art_points

tab_v=BuildFromInc([[1,2],[0,2],[1,0,3,4],[2,4],[2,3]])
tab_v=BuildFromInc([[1],[0,2],[1]])
tab_v=BuildFromInc([[1],[2],[3],[]])
print(PunktyArtykulacji(tab_v))