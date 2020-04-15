""" Kapitan  pewnego  statku zastanawia się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci  tablicy M,  gdzie M[y][x]  to  głebokość  zatoki  na  pozycji  (x, y).  Jeśli  jest  ona  większa  niż  pewna wartość int T to statek może się tam znaleźć. Początkowo statek jest na pozycji (0,0) a port znajduje się na pozycji (n−1, m−1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok  (to  znaczy,  na  pozycję,  której  dokładnie  jedna  ze  współrzędnych  różni  się  o  jeden).  Proszę  napisać funkcję rozwiązującą problem kapitana. """
""" 
Algorytm polega na:
0) Sprawdzam czy B.val>=T (Bo nie moge stac na niskiej wodzie a na B mam być obowiązkowo)
BFS przejscie po macierzy biorąc pod uwagę int T, czyli:
1) Wkładam na stos punkt A, jego dzieci (czyli takie punkty w ktorych moge sie znalezc), dzieci jego dzieci i td, dopoki nie przejde caly graf/nie bede mial dzieci lub napotkam sie na punkt B

 """
