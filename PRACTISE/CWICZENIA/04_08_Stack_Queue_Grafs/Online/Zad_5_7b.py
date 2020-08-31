""" 
Proszę podać algorytm, który mając na wejściu graf G reprezentowany przez listy sąsiedztwa sprawdza, czy dla każdej krawędzieu→vistnieje także krawędź przeciwna
 """
""" 
Lista sąsiedstwa: (Pokazuje liste wychodz z kazdego wierzchołku krawedzi)
0 -> 1,2 
1 -> None
2 -> 0,3
3 -> 2
 """

""" 
Idę BFSem po wszystkich wierzchołkach i:
    1) Ustawiam 
    v.out=1 Jak wychodze z tego jako z rodzica
    v.in=1 Jak wchodze do niego jako do dziecka
    2) Ide po wszystkich V i sprawdzam czy v.in=v.out=True, jak nie to return False
 """