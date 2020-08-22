from heapq import *
""" 
1. Implementacja na listach incydencji, wykorzystuje krotki postaci:
            (DISTANCE,INDEX,WAGA)
2. Implementacja na Macierzach Incydencji
"""
def GraphFromTabOfEddges(V,edges):
    """ 
    Inicjalizacja grafu z krotkami
    Zwraca graph
     """
    graph=[[] for _ in range(V+1)]
    for i in range(len(edges)):
        x,y,w=edges[i]
        graph[x].append((float("inf"),y,w))
        graph[y].append((float("inf"),x,w))
    return graph
def QueueOnMy(graph):
    """ 
    Building queue of distance from
    each graph vertex
    O(E)
     """
    q=[]
    for i in range(len(graph)):
        for j in graph[i]:
            heappush(q,j)
    return q
def if_inf(x):
        if x==float("inf"):
            return -1
        else:
            return x
def DijkstraAlgorithm(graph,start):
    """ 
    Dziala dla: 1) w(u,v)>=0 (Czyli nieujemne wagi)
                2) start i end to numery wierzcholków (Włączając)
    Zlozonosc : O(Elog(V))
    Polega na :
        Eksplorujemy graf od źródła i zawsze bierzemy najlepszego sąsiada, czyli tego, do którego jest najbliżej (ścieżka do niego jest optymalna), a potem aktualizujemy odległości od niego do jego sąsiadów (jeżeli ścieżka przez niego jest lepsza od poprzedniej
    Implementacja : W mojej wersji jak zmienila sie odleglosc, to wrzucam w queue ponownie, co zwieksza wspolczynnik zlozonosci, ale to beda potegi log(V), wiec ewentualnie rzad zlozonosci sie nie zmienia

     """
    q=QueueOnMy(graph)
    distance_graph=[float("inf")]*len(graph)
    distance_graph[start]=0
    przetworzony=[False]*len(graph)
    krotka=(0,start,0)
    heappush(q,krotka)
    while (len(q)>0):
        u=heappop(q)
        if not przetworzony[u[1]]:
            przetworzony[u[1]]=True
            for v in graph[u[1]]:
                if distance_graph[v[1]]>distance_graph[u[1]] + v[2]:
                    distance_graph[v[1]]=distance_graph[u[1]] + v[2]
                    przetworzony[v[1]]=False
                    ttp = u[0] + u[2]
                    v=(ttp,v[1],v[2])
                    heappush(q,v)
    
    distance_graph = list(map(if_inf,distance_graph))
    return distance_graph

def shortestReach(n, edges, s):
    """ 
    Works with duplicate edges as well
     """
    graph = GraphFromTabOfEddges(n,edges)
    tab =  DijkstraAlgorithm(graph,s) 
    return tab[1:s] + tab[s+1:]


print(shortestReach(4, [[1, 2, 5], [1, 2, 4], [1, 4, 2],[1,3,7],[2,3,2]] ,1))