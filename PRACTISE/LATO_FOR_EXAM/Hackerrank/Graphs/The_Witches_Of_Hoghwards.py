""" https://www.hackerearth.com/ru/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/the-witches-of-hegwarts-1/description/ """

""" 
Can be modified using set in visited of BFS and representation of graph
 """

class graph:
    def __init__(self, repr,is_Matrix,is_weighted=False ):
        
        self.repr = repr
        self.is_Matrix = is_Matrix
        self.is_weighted = is_weighted
        
    
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
def BFS(graph, start_v):
    if (graph.is_weighted==True):
        raise "Given Weighted Graph to BFS"
    Queue_FIFO = []
    #We can skip the part of allocating this tabs but for convinience leave it as it is
    distance = [float("inf")] * graph.get_vertex()
    
    visited = [False] * graph.get_vertex()
    distance[start_v] = 0
    visited[start_v] = True
    Queue_FIFO.append(start_v)
    while len(Queue_FIFO)!=0:
        u = Queue_FIFO.pop(0)
        for v in graph.get_incidence(u):
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                Queue_FIFO.append(v)
    return distance

def BuildGraph(k):
    """ 
    Building from the bottom to the top
     """
    k+=1
    repr = [[] for _ in range(k)]
    repr.append([])
    to_app = 1
    while (to_app <= k ):
        if to_app*2 < k:
            repr[to_app*2].append(to_app)
        if to_app*3 < k:
            repr[to_app*3].append(to_app)
        if to_app+1 < k:
            repr[to_app+1].append(to_app)
        to_app+=1
    g = graph(repr,is_weighted=False, is_Matrix=False)
    return BFS(g,k-1)[1]
class Solution:
    def __init__(self):
        n = int (input())
        for _ in range(n):
            print(self.zad(int(input())))

    def zad(self, k):
        return (BuildGraph(k))


Solution()