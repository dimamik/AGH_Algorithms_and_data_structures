""" 
Mówimy,  że  wierzchołek t w  grafie  skierowanym  jest  uniwersalnym ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź wychodząca z t. Proszę podać algorytm znajdujący ujście (jeśli istnieje) przy reprezentacji macierzowej grafu.
 """

""" 
    1.Szukam podejrzanego wierzchołku DFSem w nast sposób:
1) Zwykły DFS, ale przed tym jak się cofnąć dodaje do ostatniego elementu +1 do jakiegos .odw
2) Mam zawsze na tym elemencie konczyc rekurencje, jak .odw tego elementu (ostatniego) będzie się równać ilości wywołanych rekurencji, to:
    1) Sprawdzam warunki na ujście dla tego el
Jak nie, to:
    1) return false
    2. 
    Dla macierzy kwadratowej adjacencji
    Iterujemy po wierszach, ale nie od 0, a od tego, na ktorym skonczylismy ostatnio, bo i tak porpzednie nie spelniają warunku ujscia.
    3. 
    Obserwacja: jeżeli A[x, y] = 1, to x nie może być ujściem (bo wychodzi z niego krawędź); jeżeli A[x, y] = 0
    y nie może być ujściem (bo nie wchodzi do niego krawędź z x).

    Obserwacja 2: uniwersalne ujście może być tylko jedno.

    Rozwiązanie: zrobić stos kandydatów na ujście, na początku są to wszystkie wierzchołki. Za każdym razem
    bierzemy 2 wierzchołki z góry i sprawdzamy powyższy warunek, zawsze eliminując jeden wierzchołek.

    W n-1 krokach eliminujemy n-1 wierzchołków - O(n). Na koniec wystarczy dla jedynego pozostałego wierzchołka
    sprawdzić warunek w jego wierszu i kolumnie - O(n).

    Złożoność: O(n)
 """