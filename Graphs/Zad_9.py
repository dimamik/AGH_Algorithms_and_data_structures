""" 
1. Rozw dla grafow rzadkich:
    W sposob banalny usuwamy krawedz (x,y) i puszczamy algorytm Dijkstry z y do x, do otrzymanej odleglosci dodajemy wage krawedzi w(x,y), robimy to dla kazdej krawedzi i wybieramy najmniejszą wagę 
    (Ewentualnie mozna jakos przyspieszyc i chodzic tylko po cykli, skoro i tak bd mieli duza zlozonosc)
    --> O(E^2 logV )
2. Rozw dla grafow gestych
     Idziemy Floydem-Warshallem, dla kazdego wierzcholku probujemy przeprowadzic cykl przez kazdy inny wierzcholek w grafie i probujemy zminimalizowac Dp[i][k]+Dp[k][i]

     -> O(V^3 +(V)^2)-->O(V^3)
 """

