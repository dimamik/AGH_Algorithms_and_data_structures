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

""" DAG: SILNIE SPOJNE SKLADOWE -> duzo polaczonych acyklicznie cyklow"""

""" POMOCNICZE FUNKCJE """


""" DFS WICH RETURNS TIME """
time=0
def DFS_Usual_Visit_Time(u_index,tab_of_v):
    global time
    time+=1
    tab_of_v[u_index].visited=True
    tab_of_v[u_index].entry=time
    for v_ind in tab_of_v[u_index].tab_index_incident:
        if not tab_of_v[v_ind].visited:
            tab_of_v[v_ind].parrent=u_index
            DFS_Usual_Visit_Time(v_ind,tab_of_v)
    time+=1
    tab_of_v[u_index].process=time
    

def DFS_Time_Returns(tab_of_v):
    global time
    for v_ind in range(len(tab_of_v)):
        if not tab_of_v[v_ind].visited:
            DFS_Usual_Visit_Time(v_ind,tab_of_v)
    """ Writing out the time tab """
    tab=[0]*len(tab_of_v)
    for  i in range(len(tab_of_v)):
        tab[i]=tab_of_v[i].process
    return tab

""" tab_v=BuildFromInc([[1,4],[2],[3],[],[]])
print(DFS_Time_Returns(tab_v)) """

def OdwrocKierunekKrawedzi(tab_of_v):
    new_tab=[None]*len(tab_of_v)
    for i in range(len(tab_of_v)):
        new_tab[i]=Vertex()
    for i in range(len(tab_of_v)):
        for j in tab_of_v[i].tab_index_incident:
            new_tab[j].tab_index_incident.append(i)
    return new_tab

""" tab_v=BuildFromInc([[1,4],[2],[3],[],[]])
OdwrocKierunekKrawedzi(tab_v) """

""" DFS THAT BUILD AN ARRAY OF VERT VISITED AND WORKS WITH DECREASING TIME """
def DFS_Needed_To_Make_Array(u_index,tab_of_v,arr,times_not_sorted):
    arr.append(u_index)
    tab_of_v[u_index].visited=True
    tab_of_v[u_index].entry=time
    tab_tmp=[]*len(tab_of_v[u_index].tab_index_incident)
    for i in tab_of_v[u_index].tab_index_incident:
        """ times=[(time[i],i),(),...())] """
        tab_tmp.append(times_not_sorted[i])
    tab_tmp=sorted(tab_tmp)
    for v_ind in map(lambda item: item[1], tab_tmp):
        if not tab_of_v[v_ind].visited:
            tab_of_v[v_ind].parrent=u_index
            DFS_Needed_To_Make_Array(v_ind,tab_of_v,arr,times_not_sorted)

""" MAIN FUNCTION """
def SilneSpojneSkladowe(tab_of_v):
    """ 
    Zwraca tablice silnie spojnych skladowych
     """
    """ Get processed times """
    times=DFS_Time_Returns(tab_of_v)

    for i in range(len(times)):
        times[i]=(times[i],i)
    times_not_sorted=times
    times=sorted(times,reverse=True)

    """ Odwrocenie kierunku """
    tab_of_v=OdwrocKierunekKrawedzi(tab_of_v)

    to_ret=[]
    count=0
    """ DFS W KOLEJNOSCI MALEJACYCH CZASOW """
    for v_ind in map(lambda item: item[1], times):
        if not tab_of_v[v_ind].visited:
            arr=[]
            DFS_Needed_To_Make_Array(v_ind,tab_of_v,arr,times_not_sorted)
            to_ret.append(arr)

    return to_ret


tab_v=BuildFromInc([[1],[2,3],[0,5],[4],[5],[3]])
print(SilneSpojneSkladowe(tab_v))
