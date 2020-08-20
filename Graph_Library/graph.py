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
    def add_edge(self,u,v,w=-1):
        if (self.is_Matrix==False and self.is_weighted==False):
            self.repr[u].append(v)
        else:
            raise "NOT ADDED YET"
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
        elif (self.is_Matrix==False and self.is_weighted==True):
            tmp = []
            v = u
            for j in range(len(self.repr[v])):
                tmp.append((self.repr[v][j].index, self.repr[v][j].weight))
            return tmp
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
    def remove_edge_undirected(self,u,v):
        """ Removes edge (u,v) in E """
        if self.is_weighted==True:
            raise "NEED UNWEIGHTED GRAPH"
        if self.is_Matrix==True:
            self.repr[u][v] = 0
            self.repr[v][u] = 0
        else:
            i = 0
            while (self.is_weighted==True  and self.repr[u][i][0]!=v 
            or self.is_weighted==False and self.repr[u][i]!=v):
                i+=1
            if i<len(self.repr[u]):
                self.repr[u].remove(v)
                self.repr[v].remove(u)
            else:
                raise "NO SUCH EDGE"
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