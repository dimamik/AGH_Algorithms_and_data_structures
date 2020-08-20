""" 
Dana jest n elementowa tablica A zawierająca liczby naturalne (potencjalnie bardzo duże).
Wiadomo, że tablica A powstała w dwóch krokach. Najpierw wygenerowano losowo (z nieznanym
rozkładem) n różnych liczn nieparzystych i posortowano je rosnąco. Następnie wybrano losowo
⌈log n⌉ elementów powstałej tablicy i zamieniono je na losowo wybrane liczby parzyste. Proszę
zaproponować (bez implementacji!) algorytm sortowania tak powstałych danych. Algorytm
powinien być możliwie jak najszybszy. Proszę oszacować i podać jego złożoność czasową.
 """

""" 
1.
    1)Przeniesc liczby parzyste w inna tablice -> O(n)
    2)Posortowac liczby parzyste -> logn(log(logn))
    3)Polaczyc Mergem dwie tablicy -> O(n+logn)

 """