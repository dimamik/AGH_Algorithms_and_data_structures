""" Proszę podać algorytm “przesuwający” zadanąn-elementową tablicę A o k pozycji.  (Przesunięcie  tablicy  oznacza,  że  element,  który  był  pierwotnie  na  pozycjii,  powinien się znaleźć na pozycję n+k (modulo n). Algorytm powinien działać w miejscu """

""" 
Algorytm ZAMIANY DŁONI, k=3
        1,2,3,4,5,6
1) Rozdzielam tablice na k,(n-k)
        1,2,3|4,5,6
2) Odwracam kolejność elementów wewnątrz kawałków
        3,2,1|6,5,4
3) Zamieniam elementy całosci (0,n),(1,n-1) i td
    a)  4,2,1|6,5,3
    b)  4,5,1|6,2,3
    c)  4,5,6|1,2,3
    d)  4,5,6,1,2,3

То есть есть две руки, сначала ладонями вперед, потом поворачиваем обе ладонями к себе, и меняем местами (Так работает алгоритм)

 """