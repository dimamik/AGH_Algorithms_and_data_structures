""" 
1.Sprawdzanie czy graf nieskierowany jest dwudzielny (czyli czy da się podzielić jego wierzchołki na dwazbiory, takie że krawędzie łączą jedynie wierzchołki z różnych zbiorów).2.  Sprawdzanie czy graf nieskierowany posiada cykl. 
"""
""" 
1. Idziemy BFSem od każdego Vo in V, ale pętla if(nie_odwiedzony): Ma sie wykonac tylko dwa razy (Nie licząc wewnątrz BFS)

"""


""" 
2. Algorytm polega na DFS search, i wygląda następująco:
Dla każdego  wierzchołka sprawdzamy czy jego sąsiedzi już zostali odwiedzeni, jak tak, to graf posiada cykl, jak dla kazdego v nie - to nie posiada

 """
