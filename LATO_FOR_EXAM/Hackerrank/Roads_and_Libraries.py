""" https://www.hackerrank.com/challenges/torque-and-development/problem """



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
def BuildFromTab(tab,n):
    """ 
    
    Buduje z listy połączeń w postaci tablicy:
    tab = [[1,2],[0,1],[1,3]]
    n =4 -> ilosc wierzcholkow liczac od 0 (max_v + 1)
     """
    tab_of_v=[None]*n

    for i in range(n):
        tab_of_v[i]=Vertex()
    for i in range(len(tab)):
        tab_of_v[tab[i][0]].tab_index_incident.append(tab[i][1])
        tab_of_v[tab[i][1]].tab_index_incident.append(tab[i][0])
    return tab_of_v

""" DFS USUAL """
time=0
vert_tmp = 0
def DFS_Usual_Visit(u_index,tab_of_v):
    global time
    global vert_tmp
    time+=1

    tab_of_v[u_index].visited=True
    
    tab_of_v[u_index].entry=time
    for v_ind in tab_of_v[u_index].tab_index_incident:
        if not tab_of_v[v_ind].visited:
            vert_tmp+=1
            tab_of_v[v_ind].parrent=u_index
            DFS_Usual_Visit(v_ind,tab_of_v)
    time+=1
    tab_of_v[u_index].process=time


def DFS(tab_of_v):
    global vert_tmp
    components = 0
    vertexes = 0
    for v_ind in range(len(tab_of_v)):
        if not tab_of_v[v_ind].visited:
            components+=1
            DFS_Usual_Visit(v_ind,tab_of_v)
            vertexes+=vert_tmp
            vert_tmp=0
    """ Writing out the parrents tab """
    tab=[0]*len(tab_of_v)
    for  i in range(len(tab_of_v)):
        tab[i]=tab_of_v[i].parrent
    return components,vertexes

def roadsAndLibraries(n, c_lib, c_road, cities):
    if (c_lib < c_road):
        return c_lib * n
    for i in range(len(cities)):
        cities[i] = [cities[i][0], cities[i][1], c_road]
    tab_of_v = BuildFromTab(cities, n+1)
    number_of_sp_skl,vert = DFS(tab_of_v)
    number_of_sp_skl-=1
    money = 0
    money+=(c_lib * number_of_sp_skl)
    money+=(c_road*vert)
    return money




print(roadsAndLibraries(5, 6 ,1, [[1, 2], [1, 3], [1, 4]]))
