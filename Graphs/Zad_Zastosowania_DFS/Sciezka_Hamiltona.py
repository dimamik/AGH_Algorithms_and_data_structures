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
""" DFS USUAL """
time=0

def DFS_Usual_Visit(u_index,tab_of_v,tab_przetworzone):
    
    global time
    time+=1
    tab_of_v[u_index].visited=True
    tab_of_v[u_index].entry=time
    for v_ind in tab_of_v[u_index].tab_index_incident:
        if not tab_of_v[v_ind].visited:
            tab_of_v[v_ind].parrent=u_index
            DFS_Usual_Visit(v_ind,tab_of_v,tab_przetworzone)
    time+=1
    tab_of_v[u_index].process=time
    tab_przetworzone.append(u_index)
    if len(tab_przetworzone)==len(tab_of_v) or len(tab_przetworzone)==len(tab_of_v)+1:
        return tab_przetworzone
def DFS(tab_of_v):
    for v_ind in range(len(tab_of_v)):
        if not tab_of_v[v_ind].visited:
            tab_przetworzone=[]
            x=DFS_Usual_Visit(v_ind,tab_of_v,tab_przetworzone)
            if x!=None and x[0]==len(tab_of_v):
                return x
            else:
                for i in range(len(tab_of_v)):
                    tab_of_v[i].visited=False
    
    """ Writing out the parrents tab """
    tab=[0]*len(tab_of_v)
    for  i in range(len(tab_of_v)):
        tab[i]=tab_of_v[i].parrent
    return tab
tab_v=BuildFromInc([[2,1],[0,2],[0,1],[1,4],[3,5],[1,4]])
DFS(tab_v)