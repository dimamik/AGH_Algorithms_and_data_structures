""" 
Dany jest grafG= (V, E), gdzie każda krawędźma wagę ze zbioru{1, . . . ,|E|}(wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dladanych wierzchołkówxiysprawdza, czy istnieje ścieżka zxdoy, w której przechodzimy po krawędziach ocoraz mniejszych wagach
 """

""" 
Idziemy DFSem i:
1) Sortujemy dla kazdego wierzcholku wierzcholki po masie
2) Jak wchodzimy w wierzcholek to zapisujemy wage tam jak nie ma, jak jest, to:
    1)jak wchodzimy z wieksza wage idziemy dalej
    2)jak nie to sie cofamy i nie wchodzimy w ten wierzchołek

 """