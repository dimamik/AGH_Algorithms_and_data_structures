""" 
We have to find the path such as the maximum weight in this path is minimum

You could also use the "binary search on the answer" paradigm. That is, do a binary search on the weights, testing for each weight w whether you can find a path in the graph using only edges of weight greater than w.

The largest w for which you can (found through binary search) gives the answer. Note that you only need to check if a path exists, so just an O(|E|) breadth-first/depth-first search, not a shortest-path. So it's O(|E|*log(max W)) in all, comparable to the Dijkstra/Kruskal/Prim's O(|E|log |V|) (and I can't immediately see a proof of those, too).
 """


def BFS(repr,u,v):
    w = 0
    for i in range(len(repr[u])):
        if (repr[u][i][0] == v):
            w = repr[u][i][1]
    Q = []
    visited = [False for _ in range(len(repr))]
    Q.append(1)
    visited[1] = True
    while len(Q)>0:
        u  = Q.pop(0)
        for v in repr[u]:
            if not visited[v[0]] and v[1] <= w:
                visited[v[0]]=True
                Q.append(v[0])
    return visited[len(repr)-1],w
    pass

def getCost(g_nodes, g_from, g_to, g_weight):
    repr = [[] for _ in range(g_nodes+1)]
    for i in range(len(g_from)):
        repr[g_from[i]].append([g_to[i],g_weight[i]])
        repr[g_to[i]].append([g_from[i],g_weight[i]])
    """ 
    Using BFS for all of them, find the max-min valued path
     """
    min_path = float("inf")
    for u in range(len(repr)):
        for v in range(len(repr[u])):
            mw = BFS(repr,u,repr[u][v][0])
            if (mw[0] == True):
                min_path = min(min_path,mw[1])
    if min_path==float("inf"):
        return "NO PATH EXISTS"
    return min_path
    pass

print(getCost(5, [1, 3, 1, 4, 2] ,[2, 5, 4, 5, 3] ,[60, 70, 120, 150, 80]))
