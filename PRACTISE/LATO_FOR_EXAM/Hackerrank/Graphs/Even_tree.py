""" https://www.hackerrank.com/challenges/even-tree/problem """


def evenForest(t_nodes, t_edges, t_from, t_to):
    """ 
    graph is a tree of undirected edges
     """
    graph = [[] for _ in range(t_nodes+1)] 
    for i in range(len(t_from)):
        graph[t_from[i]].append(t_to[i])
        graph[t_to[i]].append(t_from[i])
    evens = [1 for _ in range(t_nodes+1)]
    """ Start DFS from 1 """
    visited = [False] * (t_nodes+1)
    parents = [None] * (t_nodes+1)
    def DFSVisit(graph,u):
        nonlocal visited,parents
        visited[u]=True
        for v in graph[u]:
            if not visited[v]:
                parents[v]=u
                DFSVisit(graph,v)
        if parents[u]!=None:
            evens[parents[u]]+=evens[u]
    DFSVisit(graph,1)
    c=-1
    for el in evens:
        if el%2==0:
            c+=1
    return c

print(evenForest(10, 9, [2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 1, 3, 2, 1, 2, 6, 8, 8]))
