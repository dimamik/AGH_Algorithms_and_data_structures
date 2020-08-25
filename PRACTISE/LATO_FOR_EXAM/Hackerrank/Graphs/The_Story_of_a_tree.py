""" Brute Force """
import math
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
    return parents

def storyOfATree(n, edges,k, guesses):
    tab_of_parents = []
    repr = [[] for _ in range(n+1)]
    for i in range(len(edges)):
        repr[edges[i][0]].append(edges[i][1])
        repr[edges[i][1]].append(edges[i][0])
    g = graph(repr,is_Matrix=False)
    for i in range(n+1):
        tab_of_parents.append(BFS(g,i))
    all_sum = 0
    for i in range(len(tab_of_parents)):
        c = 0
        for j in range(len(guesses)):
            if (tab_of_parents[i][guesses[j][1]] == guesses[j][0]):
                c+=1
            if (c>=k):
                all_sum+=1
                break

        
    all_sum,n = reduce_fraction(all_sum,n)
    if (all_sum>n):
        all_sum=1
        n=1
    if (all_sum==0):
        all_sum = 0
        n = 1
    return str(all_sum) + "/" + str(n)
def reduce_fraction(n,m):
        k = math.gcd(n,m)
        return (n//k, m//k)
to_ret = []
b = int(input())
for _ in range(b):
    edges = []
    n=int(input())
    for _ in range(n-1):
        nm = list(map(int,input().rstrip().split()))
        edges.append([nm[0],nm[1]])
    guesses = []
    nm = list(map(int,input().rstrip().split()))
    g = nm[0]
    k = nm[1]
    for _ in range(g):
        nm = list(map(int,input().rstrip().split()))
        guesses.append([nm[0],nm[1]])
    to_ret.append(storyOfATree(n,edges,k,guesses))

for i in range(len(to_ret)):
    print(to_ret[i])
