""" 
Dany jest graf G. Podaj jak najszybszy algorytm, który tworzy graf indukowany G’ 
zawierający taki podzbiór krawędzi i wierzchołków z G, że każdy wierzchołek w G’ 
ma stopień co najmniej k. Uwaga!: przemyśl parę razy pierwsze rozwiązanie, które 
przyjdzie Ci do głowy. 
 """
""" 
1.    przejdz po wszystkich wierzcholkach i:
        1) Usuwamy go jak jest mniej niz k i dekrementujemy stopni dzieci
    -> O(VE)
2. Wrzucic wierzcholki do maxheap po stopniach
        1) Wyjmujemy wierzcholek -> O(V-k)
        2) Patrzymy na jego sasiadow -> O(E+logV)
        3) Tak dlugo jak nie heappop() nie bedzie <k -> wtedy odrazu mamy wynik
    Dlaczego to jest szybsze:
        1) Bo mamy ElogV


 """