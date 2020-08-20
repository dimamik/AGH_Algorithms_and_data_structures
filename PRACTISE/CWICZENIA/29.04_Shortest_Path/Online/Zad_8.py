""" 
Implementacja na listach incydencji, wykorzystuje krotki postaci:
            (DISTANCE,INDEX,WAGA)

"""

def LS_Krotki_graph_init(V,E):
    """ 
    Inicjalizacja grafu z krotkami
    Zwraca graph
     """
    graph=[[] for _ in range(V)]
    for i in range(E):
        x,y,w=map(int,input().strip().split())
        graph[x].append((float("inf"),y,w))
    return graph
def BellmanaForda(graph,start,end):
    distance_graph=[float("inf")]*len(graph)
    distance_graph[start]=0
    parent_graph = [-1]*len(graph)
    """ 
    of use V instead of len(graph)-1
     """
    for u in range(len(graph)-1):
        for v in graph[u]:
            if distance_graph[v[1]]>distance_graph[u] + v[2] and (u==start or parent_graph[u][1]>v[2]):
                    distance_graph[v[1]]=distance_graph[u] + v[2]
                    parent_graph[v[1]]=[u,v[2]]
    """ print(distance_graph)
    print(parent_graph) """
    return distance_graph[end]


graph =LS_Krotki_graph_init(10,11)
print(BellmanaForda(graph,0,9))