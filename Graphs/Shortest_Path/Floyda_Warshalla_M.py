def Polacz_Wierzch_ms(tab, index_wierz):
    tab_of_wierz = []
    for i in range(len(tab)):
        if tab[index_wierz][i] != 0:
            tab_of_wierz.append(i)
    return tab_of_wierz

def Are_Connnected_in_directed_ms(tab, fw, sw):
    if fw >= len(tab) or sw >= len(tab):
        return 0
    return tab[fw][sw] != 0

def Input_MSGraph_AS_MATRIX():
    n = int(input())
    tab = [0]*n
    for i in range(len(tab)):
        tab[i] = [0]*n
    for i in range(len(tab)):
        for j in range(len(tab)):
            tab[i][j] = int(input())
    return tab

def Input_MS_Graph():
    V, E = map(int, input().strip().split())

    tab = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        x, y, w = map(int, input().strip().split())
        tab[x][y] = w
    print(tab)
    return tab


def FloydaWarshalla(graph):
    """ 
    Idea : Mamy gotowe "trasy" i dynamicznie z nich korzystamy, uzupelniajac kolejne
    Implementacja : Wystarczy zrobic 3 petli for xD
    Returns: [[0,2,...],[1,0,inf,...]], where 2 is distance from 0 to 1
    Zlozonosc -> O(V^3) -> Co jest lepiej niż Bellmana Forda -> O(V^2E) dla grafów rzadkich i lepiej niz algorytm Dijkstry O(VElogV) dla grafow gestych -> O(V^3logV)

     """
    V = len(graph)-1
    Distance = [[float("inf")]*(V+1) for _ in range(V+1)]
    for i in range(V+1):
        for j in range(V+1):
            if i == j:
                Distance[i][j] = 0
            elif graph[i][j] != 0:
                Distance[i][j] = graph[i][j]
    #print(Distance)
    for t in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                if Distance[i][j] > Distance[i][t]+Distance[t][j]:
                    Distance[i][j] = Distance[i][t]+Distance[t][j]
    print(Distance)
    return Distance


#gr = Input_MS_Graph()
g = [
    [0,2,4,2],
    [0,0,3,0],
    [0,0,0,0],
    [0,0,1,0]
]
FloydaWarshalla(g)
