def BFS( G, s ):
# G to macierz opisująca graf: G[i][j]==1 jeśli jest
# wierzchołek z i do j. W przeciwnym razie G[i][j]=0
# s to numer wierzchołka źródłowego


# tu proszę umieścić swoją implementację

# elementarny test, powinien wypisać
# [(None,0), (0,1), (0,1), (2,2)]
# lub
# [(None,0), (0,1), (0,1), (1,2)]
G = [[0,1,1,0],[0,0,0,1],[0,1,0,1], [0,0,0,0]]
print( BFS(G,0) )