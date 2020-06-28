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
def DFS_Usual_Visit_Parent_and_Wsteczne(u_index,tab_of_v):
    """ 
    DFS, zwraca tablicę krawędzi wstecznych,parrent i td
     """
    global time
    time+=1
    tab_of_v[u_index].visited=True
    tab_of_v[u_index].entry=time
    """ Żeby nie nadpisywać już zapisanych """
    tab_of_v[u_index].low=min(time,tab_of_v[u_index].low)
    for v_ind in tab_of_v[u_index].tab_index_incident:
        if not tab_of_v[v_ind].visited:
            tab_of_v[v_ind].parrent=u_index
            DFS_Usual_Visit_Parent_and_Wsteczne(v_ind,tab_of_v)    
        else:
            if tab_of_v[u_index].parrent!=v_ind:
                """ Krawędź wsteczna tu jest, bo już odwiedzony i nie rodzic"""
                tab_of_v[u_index].low=min(tab_of_v[v_ind].low,tab_of_v[u_index].entry)
                tab_of_v[u_index].wsteczna=v_ind

    time+=1
    tab_of_v[u_index].process=time

def DFS_Parent_and_Wsteczne(tab_of_v):
    for v_ind in range(len(tab_of_v)):
        if not tab_of_v[v_ind].visited:
            DFS_Usual_Visit_Parent_and_Wsteczne(v_ind,tab_of_v)
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
    return tab_time,tab_p,tab_w,tab_l

def MostyDFS(tab_of_v):
    """ Last two returns are useless in this case """
    tab_entry,tab_p,tab_w,tab_l=DFS_Parent_and_Wsteczne(tab_of_v)
    for kr_wst in tab_w:
        if kr_wst!=-1 and tab_p[kr_wst]!=-1:
            while tab_p[kr_wst]!=-1:
                tab_of_v[tab_p[kr_wst]].low=min(tab_of_v[tab_p[kr_wst]].low,
                tab_of_v[kr_wst].low)
                kr_wst=tab_p[kr_wst]
    tab_of_mosts=[]
    for i in range(len(tab_of_v)):
        if tab_p[i]!=-1 and tab_of_v[i].low==tab_of_v[i].entry:
            tab_of_mosts.append((tab_p[i],i))
    """ return tab_of_mosts """
    if tab_of_mosts==[]:
        return "No Mosts Found"
    return tab_of_mosts

""" tab_v=BuildFromInc([[1,3],[0,2],[1,3,4],[0,2,7],[2,5,6],[4,6],[4,5],[3]])
print(MostyDFS(tab_v)) """