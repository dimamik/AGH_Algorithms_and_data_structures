""" Dzmitry Mikialevich """
from zad1testy import runtests
def FloydaWarshalla(graph):
    """ 
    Idea : Mamy gotowe "trasy" i dynamicznie z nich korzystamy, uzupelniajac kolejne
    Implementacja : Wystarczy zrobic 3 petli for xD

    Zlozonosc -> O(V^3) -> Co jest lepiej niÅ¼ Bellmana Forda -> O(V^2E) dla grafÃ³w rzadkich i lepiej niz algorytm Dijkstry O(VElogV) dla grafow gestych -> O(V^3logV)

    graph -> Postać macierzowa grafu
     """
    V = len(graph)-1
    Distance = [[float("inf")]*(V+1) for _ in range(V+1)]
    Parents = [[[]]*(V+1) for _ in range(V+1)]
    for i in range(V+1):
        for j in range(V+1):
            if i == j:
                Distance[i][j] = 0
            elif graph[i][j] != -1:
                Distance[i][j] = graph[i][j]
                Parents[i][j] = i 
    for t in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                if Distance[i][j] > Distance[i][t]+Distance[t][j]:
                    Distance[i][j] = Distance[i][t]+Distance[t][j]
                    Parents[i][j] = t

    for i in range(len(Distance)):
        for j in range(len(Distance)):
            if (Distance[i][j] == 0):
                Distance[i][j] = -1
    return Distance,Parents


def jak_dojade(G, P, n, a, b):
    Distance,Parents = FloydaWarshalla(G)
    P.append(b)
    for i in range(len(Distance)):
        for j in range(len(Distance)):
            if (not i in P or not j in P):
                Distance[i][j]=-1
    for i in range(len(Distance)):
        for j in range(len(Distance)):
            if (Distance[i][j]>n):
                Distance[i][j]=-1
    new_Distance,new_Parents = FloydaWarshalla(Distance)
    if (new_Distance[a][b]==float("inf")):
        return None
    to_ret = []
    tmp_b = b
    print("DLUGOSC TRASY OTRZYMANA: ",new_Distance[a][b] )
    while (new_Parents[a][b]!=[] or Parents[a][b]!=[]):
        if (new_Parents[a][b] == Parents[a][b]):
            to_ret.append(Parents[a][b])
            b=Parents[a][b]
        elif new_Parents[a][b]!=a and new_Parents[a][b]!=[] :
            x = Parents[a][b]
            while (x not in P):
                x = Parents[a][b]
                to_ret.append(x)
                b = Parents[a][b]
        elif Parents[a][b]!=[]:
            to_ret.append(Parents[a][b])
            b = Parents[a][b]
    to_ret.append(a)
    to_ret.reverse()
    to_ret.append(tmp_b)
    return to_ret
    # tu prosze wpisac wlasna implementacje
""" G2  = [[-1,2,-1,-1,3],[2,-1,2,-1,-1],[-1,2,-1,2,-1],[-1,-1,2,-1,3],[3,-1,-1,3,-1]]
P2 = [0,2]
print(jak_dojade(G2, P2, 4, 0, 3)) """

G1  = [[-1,5,-1,2],[-1,-1,-1,-1],[5,-1,-1,5],[2,2,-1,-1]]
P1 = [2,0]
print(jak_dojade(G1, P1, 6, 2, 1))
""" runtests( jak_dojade ) """
