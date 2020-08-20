""" 
Zwykly Dijkstra ale zamiast brać sumę, bierzemy sumę logaryfmow
log(a)+log(b)=log(ab)

 """





from heapq import *
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
from math import *
def DijkstraAlgorithm(graph,start,end):
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
    parent_graph = [0]*len(graph)
    przetworzony=[False]*len(graph)
    krotka=(0,start,0)
    heappush(q,krotka)
    counter=0
    while (len(q)>0):
        u=heappop(q)
        if not przetworzony[u[1]]:
            przetworzony[u[1]]=True
            counter+=1
            for v in graph[u[1]]:
                #Relax (u,v)
                if log(10,distance_graph[v[1]])>log(10,distance_graph[u[1]]) + log(10,v[2]):
                    distance_graph[v[1]]=log(10,distance_graph[u[1]]) + log(10,v[2])
                    przetworzony[v[1]]=False
                    ttp = u[0] + u[2]
                    v=(ttp,v[1],v[2])
                    heappush(q,v)
                    parent_graph[v[1]]=u[1]
    print(distance_graph)
    print("O(",counter,")")
    print(parent_graph)
    return distance_graph[end]
graph =LS_Krotki_graph_init(6,7)
DijkstraAlgorithm(graph,0,3)