class graph:
    def __init__(self, repr,is_Matrix,is_weighted=False ):
        """ 
        A graph class to represent graph using known structures\n
        is_Matrix==True:
            We have A Matrix n*n with a M[i][j] - weight of  edge from i to j,
            or 0 in case of no vertex
                For Example: [
                    [0,0,0,1],
                    [0,0,0,0],
                    [0,0,0,1],
                    [0,0,1,0]]\n
        is_Matrix==False:
            We have a list of edges with a lists of connections:
                For Example: [
                    [1,2,3],
                    [0,2],
                    [3,0],
                    []
                ]
                For weighted ones (v,w) -> where u,v - edge of weight w
                For Example: [
                    [(1,1),(2,2),(3,1)],
                    [(0,1),(2,5)],
                    [(3,15),(0,8)],
                    []
                ]
        Example for graph:
            g = graph([
            [0, 5, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 20],
            [0, 0, 0, 0],
            ], is_Matrix=True, is_weighted=True)
            print(g) 
         """
        self.repr = repr
        self.is_Matrix = is_Matrix
        self.is_weighted = is_weighted
        self.visited = [0] * len(self.repr)
        self.parents = [-1] * len(self.repr)
        
    def add_edge(self,u,v,w=-1):
            if (self.is_Matrix==False):
                tmp = v
                if (w!=-1):
                    tmp = (v,w)
                self.repr[u].append(tmp)
            else:
                tmp = 1
                if (w!=-1):
                    tmp = w
                self.repr[u][v]=tmp
    def get_edges(self):
        """ 
        Returns number of edges
         """
        edges = 0
        if (self.is_Matrix==True):
            for i in range(len(self.repr)):
                for j in range(len(self.repr[0])):
                    if (self.repr[i][j]!=0):
                        edges+=1
        else:
            for i in range(len(self.repr)):
                edges+=len(self.repr[i])
        return edges
    def get_vertex(self):
        """ 
        Returns number of vertecies
         """
        return len(self.repr)
    def get_incidence(self,u):
        """ 
        Returns tab of childs of u (V which u is connected with)
         """
        tmp = []
        if (self.is_Matrix==True and self.is_weighted==False):
            for v in range(len(self.repr[u])):
                if (self.repr[u][v]!=0):
                    tmp.append(v)
        elif (self.is_Matrix==False and self.is_weighted==False):
            return self.repr[u]
        elif (self.is_Matrix==False and self.is_weighted==True):
            v = u
            for j in range(len(self.repr[v])):
                tmp.append((self.repr[v][j][0], self.repr[v][j][1]))
        else:
            for i in range(self.get_vertex):
                for j in range(self.get_vertex):
                    if (self.repr[i][j]!=0):
                        tmp.append(j)
        return tmp
    def __str__(self):
        """ 
        Making lists of incidence from every graph and printing it out
         """
        output = ""
        if (self.is_Matrix == False and self.is_weighted==False):
            for v in range(len(self.repr)):
                output += (str(v) + " -> " +
                           "".join(list(str(self.repr[v])))) + '\n'

        elif (self.is_Matrix == True and self.is_weighted==False):
            for u in range(len(self.repr)):
                inc = []
                for v in range(len(self.repr[0])):
                    if (self.repr[u][v] != 0):
                        inc.append(v)
                output += (str(u) + " -> " + "".join(list(str(inc)))) + '\n'
        elif (self.is_Matrix == False and self.is_weighted==True):
            output+="\n\tv -> (1,2) means that v is connected with 1 with a weight 2\n\n"
            for v in range(len(self.repr)):
                tmp = []
                for j in range(len(self.repr[v])):
                    tmp.append((self.repr[v][j].index, self.repr[v][j].weight))
                output += (str(v) + " -> " + " ".join(list(map(str,(tmp)))) + '\n')
        elif (self.is_Matrix == True and self.is_weighted==True):
            output+="\n\tv -> (1,2) means that v is connected with 1 with a weight 2\n\n"
            for v in range(len(self.repr)):
                tmp = []
                for j in range(len(self.repr[v])):
                    if self.repr[v][j]!=0:
                        tmp.append((j, self.repr[v][j]))
                output += (str(v) + " -> " + " ".join(list(map(str,(tmp)))) + '\n')
        output+="Graph has "+ str(len(self.repr)) + " vertices"+"\n"
        output+="Graph has "+ str(self.get_edges()) + " edges"
        return output
    def remove_edge_undirected(self,u,v):
        """ Removes edge (u,v) and (v,u) in E """
        
        if self.is_Matrix==True:
            self.repr[u][v] = 0
            self.repr[v][u] = 0
        else:
            if self.is_weighted==False:
                if (v in self.repr[u] ):
                    self.repr[u].remove(v)
                if (u in self.repr[v]):
                    self.repr[v].remove(u)
            else:
                if (v in list(map(lambda x: x[0],self.repr[u])) ):
                    for a,b in self.repr[u]:
                        if a==v:
                            w = b
                    self.repr[u].remove((v,b))
                if (u in list(map(lambda x: x[0],self.repr[v])) ):
                    for a,b in self.repr[v]:
                        if a==u:
                            w = b
                    self.repr[v].remove((u,w))
            
    def reverse_edges(self):
        if self.is_Matrix==True:
            graph_tmp = [[0]*self.get_vertex() for _ in range(self.get_vertex())]
            for i in range(self.get_vertex()):
                for j in range(self.get_vertex()):
                    graph_tmp[i][j] = self.repr[i][j]
            for i in range(len(graph_tmp)):
                for j in range(len(graph_tmp[0])):
                    if (graph_tmp[i][j]!=0):
                        self.repr[i][j] = 0
                        self.repr[j][i] = graph_tmp[i][j]
        else:
            graph_tmp = [[] for _ in range(self.get_vertex())]
            for i in range(len(graph_tmp)):
                for j in range(len(self.repr[i])):
                    graph_tmp[i].append(self.repr[i][j])
            if self.is_weighted==True:
                raise "NOT READY YET"
            for i in range(len(graph_tmp)):
                j = 0
                while (len(graph_tmp[i])>0):
                    tmp = graph_tmp[i][j]
                    graph_tmp[i].remove(tmp)
                    self.repr[i].remove(tmp)
                    self.repr[tmp].append(i)


def Diametr(graph,start_v=1):
    """ 
    Getting MST of a graph and returning the diametr ()
     """
    visited = [False] * graph.get_vertex()
    entry = [-1] * graph.get_vertex()
    process = [-1] * graph.get_vertex()
    parents = [-1] * graph.get_vertex()
    time = 0
    most_right = -1
    most_left = -1
    def DFSVisit(graph, u):
        nonlocal time, visited, entry, process, parents,most_right,most_left
        time += 1
        visited[u] = True
        entry[u] = time
        for v in graph.get_incidence(u):
            if not visited[v]:
                parents[v] = u
                DFSVisit(graph, v)
        time += 1
        process[u] = time
        if (most_right == -1):
            most_right = u
        elif (most_right !=-1 and most_left==-1):
            most_left = u

    DFSVisit(graph,start_v)
    visited = [False] * graph.get_vertex()
    most_left =-1
    DFSVisit(graph,most_right)
    return most_right,most_left


g = graph([
    [],
    [2,3],
    [1,3,4],
    [2,1,4,6,5],
    [2,3,6],
    [3,6],
    [4,3,5]
],is_Matrix=False,is_weighted=False)

print(Diametr(g))



def Polacz_Wierzch_ms(tab, index_wierz):
    tab_of_wierz = []
    for i in range(len(tab)):
        if tab[index_wierz][i] != 0:
            tab_of_wierz.append(i)
    return tab_of_wierz

def Are_Connnected_in_directed_ms(tab, fw, sw):
    if fw >= len(tab) or sw >= len(tab):
        return 0
    return tab[fw][sw] != 0

def Input_MSGraph_AS_MATRIX():
    n = int(input())
    tab = [0]*n
    for i in range(len(tab)):
        tab[i] = [0]*n
    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j] = int(input())
    return tab

def Input_MS_Graph():
    V, E = map(int, input().strip().split())

    tab = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y, w = map(int, input().strip().split())
        tab[x][y] = w
    print(tab)
    return tab


def FloydaWarshalla(graph):
    """ 
    Idea : Mamy gotowe "trasy" i dynamicznie z nich korzystamy, uzupelniajac kolejne
    Implementacja : Wystarczy zrobic 3 petli for xD
    Returns: [[0,2,...],[1,0,inf,...]], where 2 is distance from 0 to 1
    Zlozonosc -> O(V^3) -> Co jest lepiej niÅ¼ Bellmana Forda -> O(V^2E) dla grafÃ³w rzadkich i lepiej niz algorytm Dijkstry O(VElogV) dla grafow gestych -> O(V^3logV)

     """
    V = len(graph)-1
    Distance = [[float("inf")]*(V+1) for _ in range(V+1)]
    for i in range(V+1):
        for j in range(V+1):
            if i == j:
                Distance[i][j] = 0
            elif graph[i][j] != 0:
                Distance[i][j] = graph[i][j]
    #print(Distance)
    for t in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                if Distance[i][j] > Distance[i][t]+Distance[t][j]:
                    Distance[i][j] = Distance[i][t]+Distance[t][j]
    print(Distance)
    return Distance


#gr = Input_MS_Graph()
g = [
    [0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0],
    [0,1,0,1,1,0,0],
    [0,1,1,0,1,1,1],
    [0,0,1,1,0,0,1],
    [0,0,0,1,0,0,1],
    [0,0,0,1,1,1,0],
]
FloydaWarshalla(g)
