""" 
Dany  jest  ciąg  przedziałów  postaci      [ai, bi].  Dwa  przedziały  można skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytmy dla następujących problemów:
1.  Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
2.  Problem stwierdzenia jaki najdłuższy odcinek można uzyskać sklejając najwyżej k odcinków
 """

""" 
1. 

1) Robimy graf G=(V,E), w którym:
    V - zbiór początków i końców razem
    E (v1,v2) - wtw gdy v1 i v2 stanowią przedział
2) Idziemy DFSem z ai w bi jak sie return True, jak nie to return 0

 """


""" 
2.

Budowanie grafa takie same jak poprzednio
Zmodyfikowany BFS na najdłuższą "ścieżkę"
 """