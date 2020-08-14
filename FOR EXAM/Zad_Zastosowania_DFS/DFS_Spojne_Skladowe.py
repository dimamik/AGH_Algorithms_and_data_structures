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
    Buduje z listy sÄ…siedstwa w postaci tablicy
    Lista sÄ…siedstwa tab
    tab=[[2,3],[1,5],...]
     """
    tab_of_v=[None]*len(tab)
    for i in range(len(tab)):
        V=Vertex()
        V.tab_index_incident=tab[i]
        tab_of_v[i]=V
    return tab_of_v
def BuildFromTab(tab,n):
    """ 
    
    Buduje z listy połączeń w postaci tablicy:
    tab = [[1,2],[0,1],[1,3]]
    n =4 -> ilosc wierzcholkow liczac od 0 (max_v + 1)
     """
    tab_of_v=[None]*n
    for i in range(n):
        V = Vertex()
        tmp = []
        for j in range(len(tab)):
            if (tab[j][0]==i ):
                tmp.append(tab[j][1])
            elif (tab[j][1]==i):
                tmp.append(tab[j][0])
        V.tab_index_incident=tmp
        tab_of_v[i]=V
    return tab_of_v

""" DFS USUAL """
time=0
def DFS_Usual_Visit(u_index,tab_of_v):
    global time
    time+=1
    tab_of_v[u_index].visited=True
    tab_of_v[u_index].entry=time
    for v_ind in tab_of_v[u_index].tab_index_incident:
        if not tab_of_v[v_ind].visited:
            tab_of_v[v_ind].parrent=u_index
            DFS_Usual_Visit(v_ind,tab_of_v)
    time+=1
    tab_of_v[u_index].process=time

def DFS(tab_of_v):
    components = 0
    for v_ind in range(len(tab_of_v)):
        if not tab_of_v[v_ind].visited:
            components+=1
            DFS_Usual_Visit(v_ind,tab_of_v)
    """ Writing out the parrents tab """
    tab=[0]*len(tab_of_v)
    for  i in range(len(tab_of_v)):
        tab[i]=tab_of_v[i].parrent
    return components
tab_v=BuildFromTab([[1,2],[2,3],[4,5],[5,6],[1,3]],7)
""" tab_v=BuildFromInc([[],[2,3],[1,3],[2,1],[5],[4,6],[5]]) """
print(DFS(tab_v))