""" 
Dzmitry Mikialevich
 """

max_road = 0 

class Node:
    def __init__(self):
        self.children = 0          
        self.child = []
        self.max_road_down = 0              # ustawiamy 0, bo czasem lepiej nie schodzić do dołu
        self.second_max_road_down = 0       # pierwsza zmienna to maksymalna ścieżka w dół, second - druga max

def heavy_path(T): # zakładamy, że T - to korzeń drzewa
    global max_road

    for kid in T.child:
        if kid[0].children == 0:    # jeżeli to liść
            
            if T.max_road_down < kid[1]:     # sprawdzamy aktulne znaczenie z drogą do liścia
                T.second_max_road_down = T.max_road_down
                T.max_road_down = kid[1]
                
                if max_road < T.max_road_down:   # jeżeli aktulna droga jest lepsza od max_road, to zmieniamy
                    max_road = T.max_road_down

        else: # czyli liczność dzieci większa niż 0
            result = heavy_path(kid[0])             # wywołujemy dla dzieci, nigdy nie wywołamy dla jednego wierzchołka
            if T.max_road_down < result + kid[1]:# kilka razy, dlatego nie potrzebna jest zmienna typu visited
                T.second_max_road_down = T.max_road_down
                T.max_road_down = result + kid[1]

                if max_road < T.max_road_down: # jeżeli aktulna droga jest lepsza od max_road, to zmieniamy
                    max_road = T.max_road_down

    if max_road < T.max_road_down + T.second_max_road_down: # jeżeli jest lepiej z jednego liścia przejść
        max_road = T.max_road_down + T.second_max_road_down # przez ten wierzchołek do innego, to tu
                                                                  # to zostanie zaktualizowane  
    return T.max_road_down   # zwracamy to dla rekurencji, sama wartość końcowa w max_road

""" 
--> O(n)
 """
A = Node()
B = Node()
B.children = 0
C = Node()
C.children = 0
A.children = 2
A.child = [ (B,5), (C,-1) ]
heavy_path(A)



