""" 
Jak posortować n-elementową tablicę liczb rzeczywistych, które przyjmują tylko log n różnych
wartości? Uzasadnić poprawność algorytmu i oszacować złożoność. (Nie trzeba implementować). """


""" 
1. Pierwszy warjant rozwiązania - Użycie Hash Tables

2. 
    1) Alokujemy  tablice krotek (struktur) rozmiaru logn (tab_of_value, tab_of_counts)
    2) Przechodzimy po glownej teblicy i dla kazdego elementu w niej szukamy miejsca w tablice tab_of_value uzywając binary search (O(nlog(logn)))
        1) Jak tego elementu nie ma lub pod jego idexem znajduje sie inny element to przesuwamy tablice o 1 w prawo, jak ten elemnt juz jest -> inkrementujemy licznik w krotce
    3) Przechodzimy po countach i robimy posortowana tablice

    Ogolna zamortyzowana zlozonosc (O(n(log(logn))))
3. Algorytm Quicker sort, w ktorym dzielimy na :
        Mniejsze niz pivot
        Wieksze niz pivot
        Rowne pivotu
        
 """