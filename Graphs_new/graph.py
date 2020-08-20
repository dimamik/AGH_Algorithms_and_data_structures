class PseudoVertex():
        """ 
        Help-class to handle if (is_weighted==True and is_Matrix == False) case
         """
        def __init__(self, index=-1, weight=-1):
            self.index = index
            self.weight = weight
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
                raise "NOT READY YET"4
            for i in range(len(graph_tmp)):
                j = 0
                while (len(graph_tmp[i])>0):
                    tmp = graph_tmp[i][j]
                    graph_tmp[i].remove(tmp)
                    self.repr[i].remove(tmp)
                    self.repr[tmp].append(i)


def BFS(graph, start_v):
    """ 
    Searching Algorithm working in Breadth, works only with non-weighted vertecies\n
    ->O(V+E)
    Returns: distance,parents\n
    For given non-weighted graph and start_v returns distance from start_v to each of the other vertecies and parents in this distance.
        Is based on the fact that there is no shorter path than current because of the equal weights.
        Can be improved and transformated to the weighted but small integers by dividing into the ones with weight=1\n
    Test Cases For BFS
        g1 = graph([
            [1,3,4],
            [3],
            [5],
            [5],
            [2,5],
            []
        ],is_Matrix=False)
        g2 = graph([
            [0,1,1,1],
            [0,0,1,0],
            [0,0,0,0],
            [0,0,0,0]
        ],is_Matrix=True)
        BFS(g2,1) 
     """
    if (graph.is_weighted==True):
        raise "Given Weighted Graph to BFS"
    Queue_FIFO = []
    #We can skip the part of allocating this tabs but for convinience leave it as it is
    distance = [float("inf")] * graph.get_vertex()
    parents = [-1] * graph.get_vertex()
    visited = [False] * graph.get_vertex()
    distance[start_v] = 0
    visited[start_v] = True

    parents[start_v] = start_v
    Queue_FIFO.append(start_v)
    while len(Queue_FIFO)!=0:
        u = Queue_FIFO.pop(0)
        for v in graph.get_incidence(u):
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parents[v] = u
                Queue_FIFO.append(v)
    return distance,parents
def BFS_01(graph,start_v):
    """ 
    Given graph with 0/1 weights
    Finding the shortest path from start_v to each other vertex
    Using double queue and put 0 vertecies to begining and 1 to the end\n
    Returns: shortest distance from start_v to each of V\n
    g3 = graph([
    [(1,1),(2,0)],
    [(0,1),(2,0)],
    [(0,0),(1,0)]
    ],is_Matrix=False,is_weighted=True)
    BFS_01(g3,0)
    g4 = graph([
    [],
    [(2,1)],
    [(1,1),(3,1),(4,0)],
    [(2,1),(4,1),(6,0)],
    [(2,0),(3,1),(5,1)],
    [(4,1),(6,1)],
    [(5,1)]
    ],is_Matrix=False, is_weighted=True)
    BFS_01(g4,1)
     """
    Double_Queue = []
    #We can skip the part of allocating this tabs but for convinience leave it as it is
    distance = [float("inf")] * graph.get_vertex()
    parents = [-1] * graph.get_vertex()
    visited = [False] * graph.get_vertex()
    distance[start_v] = 0
    visited[start_v] = True
    parents[start_v] = start_v
    Double_Queue.append(start_v)
    while len(Double_Queue)!=0:
        u = Double_Queue.pop(0)
        for v in graph.get_incidence(u):
            w = v[1]
            v = v[0]
            if not visited[v] or distance[v] > distance[u] + w:
                visited[v] = True
                distance[v] = distance[u] + w
                parents[v] = u
                if (w==0):
                    Double_Queue.insert(0,v)
                else:
                    Double_Queue.append(v)
    return distance,parents
def DFS(graph,start_v=0):
    """ 
    Searching in depth algorithm
    O(V+E)\n
    Can be used in various of situations like topological sort,finding mosts, etc.
    Returns: parents,process, where process is time when i=v (process[i]) is processed\n
    g1 = graph([
    [1,3,4],
    [3],
    [5],
    [5],
    [2,5],
    []
    ],is_Matrix=False)
    DFS(g1,0)
     """
    visited = [False] * graph.get_vertex()
    entry = [-1] * graph.get_vertex()
    process = [-1] * graph.get_vertex()
    parents = [-1] * graph.get_vertex()
    time = 0
    def DFSVisit(graph,u):
        nonlocal time,visited,entry,process,parents
        time+=1
        visited[u]=True
        entry[u]=time
        for v in graph.get_incidence(u):
            if not visited[v]:
                parents[v]=u
                DFSVisit(graph,v)
        time+=1
        process[u]=time 
    DFSVisit(graph,start_v)
    for v in range(graph.get_vertex()):
        if not visited[v]:
            DFSVisit(graph,v)
    return parents,process
def Topological_Sort(graph):
    """ 
    Sorting vertecies such thah if (u,v) in E, than u < v
    Using Usual DFS and append to begining the processed vertecies\n
    -> O(V + E)\n
    Returns: v in sorted order
        [5,0,1,2,3,4]
    Example:
        g = graph([[1,2],[],[1,3,4],[1,4],[0]], is_Matrix=False, is_weighted=False)
        print(Topological_Sort)
     """
    visited = [False] * graph.get_vertex()
    sorted_vertecies = []

    def DFSVisit(graph, u):
        nonlocal visited, sorted_vertecies
        visited[u] = True
        for v in graph.get_incidence(u):
            if not visited[v]:
                DFSVisit(graph, v)
        sorted_vertecies.insert(0, u)
    for v in range(graph.get_vertex()):
        if not visited[v]:
            DFSVisit(graph, v)
    return sorted_vertecies
def Euler_Cycle(graph):
    """ 
    Have undirected graph and mark edges as visited not vertecies
    Return: The path in Euler Cycle 
    [0,1,2,3,4,5,6,0] -> path
    \n
    -> O(V + E)\n
    Example:
        Wyklad_8_2_Graph = graph([
        [1,5],
        [0,5,6,2],
        [1,6,4,3],
        [2,4],
        [5,6,2,3],
        [0,1,6,4],
        [1,2,4,5]
        ],is_Matrix=False, is_weighted=False)
        print(Euler_Cycle(Wyklad_8_2_Graph))
     """
    visited = [False] * graph.get_vertex()
    Queue_FILO = []
    edges_tmp = graph.get_edges()//2
    prev_call = -1
    def DFSVisit(graph,u):
        nonlocal visited
        nonlocal prev_call
        for v in graph.get_incidence(u):
            if v == prev_call:
                continue
            if not visited[v]:
                graph.remove_edge_undirected(u,v)
                prev_call = u
                DFSVisit(graph,v)
        if (graph.get_incidence(u) == []):
            visited[u] = True
        Queue_FILO.insert(0,u)

    DFSVisit(graph,0)
    if len(Queue_FILO)!=edges_tmp+1:
        raise "BLAD"
    return Queue_FILO



g = graph([
    [(1,2)],
    [(0,3)]
],is_Matrix=False,is_weighted=True)
g.remove_edge_undirected(0,1)
print(g)

def Silnie_Spojne_Skladowe(graph):
    """ 
    Strongly Connected Components\n
    https://en.wikipedia.org/wiki/Strongly_connected_component

    -> O(V + E)\n
    Algorithm:
        1. Use DFS to get times of processing of eqch vertex
        2. Sort by the time of processing in decreasing order
        3. Reverse every edge
        4. DFS in decreasing time of processing and when v is entered by DFS, append it to this component. 
            P.S. Each new DFS from main function creates new component
    Return:
        tab = [[0,1,2], [4,5], [3,6]], where 0,1,2 is v in strongly connected component and so on
        len(tab) - how many of them there are in graph
    Example:
        g5 = graph(
        [[1],
        [2, 3],
        [0, 5],
        [4], [5],
        [3]
        ],is_Matrix=False
        )
        Silnie_Spojne_Skladowe(g5) 
     """
    usless,times = DFS(graph)
    for i in range(len(times)):
        times[i]=(times[i],i)
    times_not_sorted=times[:]
    times=sorted(times,reverse=True)
    visited = [False] * graph.get_vertex()
    entry = [-1] * graph.get_vertex()
    process = [-1] * graph.get_vertex()
    components = []
    time = 0
    graph.reverse_edges()
    
    def DFS_Needed_To_Make_Array(u_index,arr):
        """ DFS THAT BUILD AN ARRAY OF VERT VISITED AND WORKS WITH DECREASING TIME """
        nonlocal visited,times_not_sorted,graph,entry,time
        arr.append(u_index)
        visited[u_index]=True
        entry[u_index]=time
        tab_tmp=[]
        for i in graph.get_incidence(u_index):
            tab_tmp.append(times_not_sorted[i])
        tab_tmp=sorted(tab_tmp)
        for v_ind in map(lambda item: item[1], tab_tmp):
            if not visited[v_ind]:
                DFS_Needed_To_Make_Array(v_ind,arr)

    for v_ind in map(lambda item: item[1], times):
        if not visited[v_ind]:
            arr=[]
            DFS_Needed_To_Make_Array(v_ind,arr)
            components.append(arr)
    return components


def Mosty_DFS(graph):
    """ 
    Input: graph nie skierowany nie ważony
    Most -> krawedz, usuniecie ktorej powoduje rozspujnienie grafu\n
    Returns: [(2, 4), (3, 7)], where 2,4 -> is an edge

    O(V + E)\n
    Example:
        g = graph([[1, 3], [0, 2], [1, 3, 4], [0, 2, 7], [2, 5, 6], [
        4, 6], [4, 5], [3]], is_Matrix=False, is_weighted=False)
        print(Mosty_DFS(g))
     """
    def DFS_With_Low(graph):
        time = 0
        visited = [False] * graph.get_vertex()
        parents = [-1] * graph.get_vertex()
        entry = [-1] * graph.get_vertex()
        low = [-1] * graph.get_vertex()
        wsteczna = [-1] * graph.get_vertex()
        process = [-1] * graph.get_vertex()

        def DFS_Visit(u_index, graph):
            nonlocal time, visited, parents, entry, low, wsteczna, process
            time += 1
            visited[u_index] = True
            entry[u_index] = time
            """ Default wartosc low """
            low[u_index] = time
            for v_ind in graph.get_incidence(u_index):
                if not visited[v_ind] == True:
                    parents[v_ind] = u_index
                    DFS_Visit(v_ind, graph)
                    """ Podnosze wartosc w gore drzewa DFS """
                    low[u_index] = min(
                        low[v_ind], low[u_index])
                else:
                    if parents[u_index] != v_ind:
                        """ Krawędź wsteczna tu jest, bo już odwiedzony i nie rodzic,
                        wiec uaktualizujemy low"""
                        """ !!!UWAGA PORÓWNUJE Z ENTRY WSTECZNYM A NIE LOW!!! """
                        low[u_index] = min(low[u_index], entry[v_ind])
                        wsteczna[u_index] = v_ind
            time += 1
            process[u_index] = time

        for v_ind in range(graph.get_vertex()):
            if not visited[v_ind]:
                DFS_Visit(v_ind, graph)
        return entry, parents, low

    entry, parents, low = DFS_With_Low(graph)
    tab_of_mosts = []
    for i in range(graph.get_vertex()):
        if parents[i] != -1 and low[i] == entry[i]:
            tab_of_mosts.append((parents[i], i))
    if tab_of_mosts == []:
        return "No Mosts Found"
    return tab_of_mosts



