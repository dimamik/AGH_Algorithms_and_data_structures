""" 
1.Sprawdzanie czy graf nieskierowany jest dwudzielny (czyli czy da się podzielić jego wierzchołki na dwazbiory, takie że krawędzie łączą jedynie wierzchołki z różnych zbiorów).2.  Sprawdzanie czy graf nieskierowany posiada cykl. 
"""
""" 
1. Using BFS
1. Following is a simple algorithm to find out whether a given graph is Birpartite or not using Breadth First Search (BFS).
1. Assign RED color to the source vertex (putting into set U).
2. Color all the neighbors with BLUE color (putting into set V).
3. Color all neighbor’s neighbor with RED color (putting into set U).
4. This way, assign color to all vertices such that it satisfies all the constraints of m way coloring problem where m = 2.
5. While assigning colors, if we find a neighbor which is colored with same color as current vertex, then the graph cannot be colored with 2 vertices (or graph is not Bipartite)

"""


""" 
2. Algorytm polega na DFS search, i wygląda następująco:
Dla każdego  wierzchołka sprawdzamy czy jego sąsiedzi już zostali odwiedzeni, jak tak, to graf posiada cykl, jak dla kazdego v nie - to nie posiada

 """
