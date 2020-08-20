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