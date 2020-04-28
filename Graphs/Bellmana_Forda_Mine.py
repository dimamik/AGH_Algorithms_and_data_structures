""" 
Implementacja na listach incydencji, wykorzystuje krotki postaci:
            (DISTANCE,INDEX,WAGA)

] """

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
    """ 
    Dziala dla: 1) w(u,v) in RR (Czyli wszystkie wagi)
                2) start i end to numery wierzcholków (Włączając)
                3) Wykrywa negatywne cykli
    Zlozonosc : O(EV) - Worst Case
                O(E)  - Best Case 
    Polega na :
     """
    distance_graph=[float("inf")]*len(graph)
    distance_graph[start]=0
    parent_graph = [0]*len(graph)
    """ 
    of use V instead of len(graph)-1
     """
    for u in range(len(graph)-1):
        for v in graph[u]:
            if distance_graph[v[1]]>distance_graph[u] + v[2]:
                    distance_graph[v[1]]=distance_graph[u] + v[2]
                    parent_graph[v[1]]=u
    print(distance_graph)
    print(parent_graph)
    """ Cheking for cykle """
    for u in range(len(graph)):
        for v in graph[u]:
            if distance_graph[v[1]]>distance_graph[u] + v[2]:
                return False
    return True
graph =LS_Krotki_graph_init(4,4)
print(BellmanaForda(graph,0,3))


        
            