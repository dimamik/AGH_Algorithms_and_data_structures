from zad1testy import runtests
from heapq import *
""" Dzmitry Mikialevich """

""" 
Dziala w czasie O(V^2) i polega na rozbiciu wierzcholku na 3 odpowiadajace drodze, po ktorej dostalismy w ta wyspe. Dalej wierzcholki sa polaczone gdy maja rozne drogi (Podobno do zadania z kobieta i chlopakiem jadacym na przemian)
Mozna zaimplementowac Dijkstre, wtedy bedzie szybciej
 """

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
    """ print(distance_graph)
    print("O(",counter,")")
    print(parent_graph) """
    return min(distance_graph[end],distance_graph[end+1],distance_graph[end+2])


def islands(G, A, B):
    """ Recombine the graph """

    """ Replace 0 with -1 """
    for i in range(len(G)):
        for j in range(len(G)):
            if (G[i][j]==0):
                G[i][j]=-1
    new_G = [[-1] * (3*len(G)) for _ in range(3*len(G))] 
    """ 
    0/1/2 + 3 * nr_wierz  = index in new_G
     """
    for i in range(len(G)):
        for j in range(len(G)):
            if (G[i][j] != -1):
                if (G[i][j] == 1):
                    new_G[3*i][1+3*j] = 1
                    new_G[3*i][2+3*j] = 1
                    pass
                elif (G[i][j] == 5):
                    new_G[1 + 3*i][3*j] = 5
                    new_G[1+3*i][2+3*j] = 5
                    pass
                elif (G[i][j] == 8):
                    new_G[2 + 3*i][3*j] = 8
                    new_G[2+3*i][1+3*j] = 8
                    pass
    max_w = min(DijkstraAlgorithm(new_G,0 + A*3 ,B*3 ),DijkstraAlgorithm(new_G,1+A*3,B*3),DijkstraAlgorithm(new_G,2+A*3,B*3))
    return max_w
        
G1 = [ [0,5,1,8,0,0,0 ],
       [5,0,0,1,0,8,0 ],
       [1,0,0,8,0,0,8 ],
       [8,1,8,0,5,0,1 ],
       [0,0,0,5,0,1,0 ],
       [0,8,0,0,1,0,5 ],
       [0,0,8,1,0,5,0 ] ]

runtests( islands ) 
