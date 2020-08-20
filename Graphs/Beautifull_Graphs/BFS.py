from Graph_Library.graph import *

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
    """ We can skip the part of allocating this tabs but for convinience leave it as it is """
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
print(BFS(g2,1) )