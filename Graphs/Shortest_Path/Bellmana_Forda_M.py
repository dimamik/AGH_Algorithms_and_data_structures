""" 
1.Implementacja na listach incydencji, wykorzystuje krotki postaci:
            (DISTANCE,INDEX,WAGA)
            
2. Implementacja na macierzach

] """


def LS_Krotki_graph_init(V, E):
    """ 
    Inicjalizacja grafu z krotkami
    Zwraca graph
     """
    graph = [[] for _ in range(V)]
    for i in range(E):
        x, y, w = map(int, input().strip().split())
        graph[x].append((float("inf"), y, w))
    return graph


def BellmanaForda(graph, start, end):
    """ 
    Dziala dla: 1) w(u,v) in RR (Czyli wszystkie wagi)
                2) start i end to numery wierzcholków (Włączając)
                3) Wykrywa negatywne cykli
    Polega na : Przechodzeniu !!po wszystkich!! wierzcholkach i robieniu Relaksacji
    Zlozonosc : O(EV) - Worst Case
                O(E)  - Best Case 
     """
    distance_graph = [float("inf")]*len(graph)
    distance_graph[start] = 0
    parent_graph = [0]*len(graph)
    """ 
    of use V instead of len(graph)-1
     """
    for u in range(len(graph)-1):
        for v in graph[u]:
            if distance_graph[v[1]] > distance_graph[u] + v[2]:
                distance_graph[v[1]] = distance_graph[u] + v[2]
                parent_graph[v[1]] = u
    print(distance_graph)
    print(parent_graph)
    """ Cheking for cykle """
    for u in range(len(graph)):
        for v in graph[u]:
            if distance_graph[v[1]] > distance_graph[u] + v[2]:
                return False
    return True
#graph =LS_Krotki_graph_init(4,4)
#print(BellmanaForda(graph,0,3))


""" Bellmana Forda na Macierzy """


def BellmanaForda(graph, start, end):
    """ 
    Dziala dla: 1) w(u,v) in RR (Czyli wszystkie wagi)
                2) start i end to numery wierzcholków (Włączając)
                3) Wykrywa negatywne cykli
    Polega na : Przechodzeniu !!po wszystkich!! wierzcholkach i robieniu Relaksacji
    Zlozonosc : O(EV) - Worst Case
                O(E)  - Best Case 
     """
    distance_graph = [float("inf")]*len(graph)
    distance_graph[start] = 0
    parent_graph = [0]*len(graph)
    """ 
    of use V instead of len(graph)-1
     """

    for i in range(len(graph)):
        for j in range(len(graph)):
            if (graph[i][j] != -1 and distance_graph[j] > distance_graph[i] + graph[i][j]):
                distance_graph[j] = distance_graph[i] + graph[i][j]
                parent_graph[j] = i

    print(distance_graph)
    print(parent_graph)
    """ Cheking for cykle """
    for i in range(len(graph)):
        for j in range(len(graph)):
            if (graph[i][j] != -1 and distance_graph[j] > distance_graph[i] + graph[i][j]):
                raise("CYKLE")
                return True
    return False


G1 = [[0, 5, 1, 8, 0, 0, 0],
      [5, 0, 0, 1, 0, 8, 0],
      [1, 0, 0, 8, 0, 0, 8],
      [8, 1, 8, 0, 5, 0, 1],
      [0, 0, 0, 5, 0, 1, 0],
      [0, 8, 0, 0, 1, 0, 5],
      [0, 0, 8, 1, 0, 5, 0]]

#print(BellmanaForda(G1,0,3))
