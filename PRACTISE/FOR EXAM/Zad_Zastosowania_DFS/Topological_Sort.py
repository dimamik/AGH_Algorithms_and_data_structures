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
        self.entry=-1
        self.process=-1
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


""" TOPOLOGICAL SORT """
time = 0
def Topologic_Sort_DFS_Visited(u_index,tab_of_v,Topologic_Sort):
    global time
    time+=1
    tab_of_v[u_index].visited=True
    tab_of_v[u_index].entry=time
    for v_ind in tab_of_v[u_index].tab_index_incident:
        if not tab_of_v[v_ind].visited:
            tab_of_v[v_ind].parrent=u_index
            Topologic_Sort_DFS_Visited(v_ind,tab_of_v,Topologic_Sort)
    time+=1
    tab_of_v[u_index].process=time
    Topologic_Sort.append(u_index)

def Topologic_Sort_DFS(tab_of_v):
    time=0
    Topologic_Sort=[]
    for v_ind in range(len(tab_of_v)):
        if not tab_of_v[v_ind].visited:
            Topologic_Sort_DFS_Visited(v_ind,tab_of_v,Topologic_Sort)
    Topologic_Sort.reverse()
    return Topologic_Sort


tab_v=BuildFromInc([[[],[2],[3],[4],[5],[]]])
tab_v=BuildFromInc([[1,2],[],[1,3,4],[1,4],[0]])
print(Topologic_Sort_DFS(tab_v))

