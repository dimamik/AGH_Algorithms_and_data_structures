""" 
Dany jest bardzo duży graf ważony, z małymi (<= 10) całkowitymi wagami dodatnimi. 
Podaj algorytm, który znajdzie najkrótsze ścieżki, do wszystkich wierzchołków, od 
wybranego startowego. 
 """

""" 
Zadanie było w odcinku 1 Wstep z wykladu pr Faliszewskiego 
http://home.agh.edu.pl/~faliszew/asd2020.html

    Robimy zwykłego BFSa w sposob nast:
        1)rozdzielając wierzchołki odpowiednio wagam ( -*-*-*-) dla wagi np 3
        2)Tworzymy na krawedzi tyle dodatkowych wierzcholkow ile wynosi waga krawedzi
        3) Puszczamy BFSa od start do end, czyli będziemy mieli zlozonosc
            O(10*V+10*E) -> O(V)
    Szczegóły implementacji:
        1) Wkladamy w kolejke (wierzcholek,waga) i zdejmujemy dopoki nie bedzie tam (wierz,0), wtedy zdejmujemy ostatecznie

 """