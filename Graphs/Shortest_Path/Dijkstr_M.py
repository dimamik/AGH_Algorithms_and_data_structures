from heapq import *
""" 
1. Implementacja na listach incydencji, wykorzystuje krotki postaci:
            (DISTANCE,INDEX,WAGA)
2. Implementacja na Macierzach Incydencji
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
                if distance_graph[v[1]]>distance_graph[u[1]] + v[2]:
                    distance_graph[v[1]]=distance_graph[u[1]] + v[2]
                    przetworzony[v[1]]=False
                    ttp = u[0] + u[2]
                    v=(ttp,v[1],v[2])
                    heappush(q,v)
                    parent_graph[v[1]]=u[1]
    print(distance_graph)
    print("O(",counter,")")
    print(parent_graph)
    return distance_graph[end]
#graph =LS_Krotki_graph_init(4,3)
#DijkstraAlgorithm(graph,0,3)


""" Implementacja na macierzach incydencji """

def DijkstraAlgorithm(graph,start,end):
    """ 
    Dziala dla: 1) w(u,v)>=0 (Czyli nieujemne wagi)
                2) start i end to numery wierzcholków (Włączając)
    Zlozonosc : O(Elog(V))
    Polega na :
        Eksplorujemy graf od źródła i zawsze bierzemy najlepszego sąsiada, czyli tego, do którego jest najbliżej (ścieżka do niego jest optymalna), a potem aktualizujemy odległości od niego do jego sąsiadów (jeżeli ścieżka przez niego jest lepsza od poprzedniej
    Implementacja : W mojej wersji jak zmienila sie odleglosc, to wrzucam w queue ponownie, co zwieksza wspolczynnik zlozonosci, ale to beda potegi log(V), wiec ewentualnie rzad zlozonosci sie nie zmienia

     """
    q=[]
    distance_graph=[float("inf")]*len(graph)
    distance_graph[start]=0
    parent_graph = [0]*len(graph)
    przetworzony=[False]*len(graph)
    heappush(q,start)
    counter=0
    while (len(q)>0):
        u=heappop(q)
        if not przetworzony[u]:
            przetworzony[u]=True
            counter+=1
            for v in range(len(graph)):
                if (graph[u][v]==0 or graph[u][v]==-1):
                    """ !!UWAGA TU!! """
                    continue
                #Relax (u,v)
                if distance_graph[v]>distance_graph[u] + graph[u][v]:
                    distance_graph[v]=distance_graph[u] + graph[u][v]
                    przetworzony[v]=False
                    heappush(q,v)
                    parent_graph[v]=u
    print(distance_graph)
    print("O(",counter,")")
    print(parent_graph)
    return distance_graph[end]


""" G1 = [ [0,5,1,8,0,0,0 ],
       [5,0,0,1,0,8,0 ],
       [1,0,0,8,0,0,8 ],
       [8,1,8,0,5,0,1 ],
       [0,0,0,5,0,1,0 ],
       [0,8,0,0,1,0,5 ],
       [0,0,8,1,0,5,0 ] ]
DijkstraAlgorithm(G1,0,3) """





