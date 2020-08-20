""" 
Dana jest mapa kraju w postaci grafu G= (V, E). Kierowca chce przejechaćz miasta (wierzchołka)sto miastat. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma takąsamą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczbyopłat. W ogólności grafGjest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.
"""
    
""" 
1. BFSem przechodzimy po wierzcholkach i korzystamy z DoubleQueue, łóżmy dzieci w nast sposob:
0 z prawej strony, jedynki z lewej. Zdejmujemy z prawej strony i tak dalej. Nasze miasto bedzie pierwszy raz odwiedzone poprzez "najkrotsza sciezke"

"""
