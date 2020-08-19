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

         """
        self.is_Matrix = is_Matrix
        self.repr = repr
        self.is_weighted = is_weighted
        self.visited = [0] * len(self.repr)
        self.parents = [-1] * len(self.repr)
        if (is_weighted == True and is_Matrix == False):
            """ Making PseudoVertex to store weights """
            for i in range(len(self.repr)):
                for j in range(len(self.repr[i])):
                    self.repr[i][j] = PseudoVertex(
                        self.repr[i][j][0], self.repr[i][j][1])
    def get_edges(self):
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
        return len(self.repr)
    def get_incidence(self,u):
        if (self.is_Matrix==True and self.is_weighted==False):
            tmp = []
            for v in range(len(self.repr[u])):
                if (self.repr[u][v]!=0):
                    tmp.append(v)
            return tmp
        elif (self.is_Matrix==False and self.is_weighted==False):
            return self.repr[u]
        else:
            raise "NOT ADDED YET"
    def get_vertex_tab(self):
        return range(self.get_vertex())
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

""" g = graph([
    [0, 5, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 20],
    [0, 0, 0, 0],
], is_Matrix=True, is_weighted=True)

print(g) """


def BFS(graph, start_v):
    """ 
    Searching Algorithm working in Breadth 
    O(V+E)
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

def DFS(graph,start_v):
    """ 
    Searching in depth algorithm
    O(V+E)\n
    Can be used in various of situations like topological sort,finding mosts, etc.
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
    for v in graph.get_vertex_tab():
        if not visited[v]:
            DFSVisit(graph,v)
    return parents


g1 = graph([
[1,3,4],
[3],
[5],
[5],
[2,5],
[]
],is_Matrix=False)

DFS(g1,0)