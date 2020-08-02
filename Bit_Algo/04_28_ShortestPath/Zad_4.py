""" 
W miasteczku są sklepy i domy. Trzeba sprawdzić jak daleko do najbliższego sklepu 
mają mieszkańcy.  
struct Vertex { bool shop; // true-sklep, false-dom  
int* distances; // tablica odległości do innych wierzchołków  
int* edges; // numery wierzchołków opisanych w distances  
int edge; // rozmiar tablicy distances (i edges)  
int d store; // odległość do najbliższego sklepu  
};  
Zaimplementować funkcję distanceToClosestStore (int n, Vertex* village) 
uzupełniającą d store dla tablicy Vertexów i oszacować złożoność algorytmu.  """

""" 
1. Tworzymy zamiast wszystkich sklepow jeden duzy ze wszystkimi krawedziami malych sklepow
Dalej puszczamy Dijkstra z tego duzego wierzcholku
    ->??O(V+E*logD)??, gdzie D->ilosc domow

 """