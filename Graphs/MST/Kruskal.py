""" 
1. Posortuj krawędzi rosnącopo wagach
2. A = ()
3. for v in V:
    make_union(V)
4. for e in RosnacyPorzadek_E: (E=(u,v))
    if find_set(u)!=find_set(v):
        A=A+e
        union(u,v)

-->O(ElogV)

 """

""" 
Implementacja:
1. Lepiej idzie przez listy sądiedstwa + E sortowac w (u,v,waga)

2. ...
 """