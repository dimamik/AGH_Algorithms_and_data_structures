""" 
Zadanie 6. 
Dany jest graf ważony z dodatnimi wagami. Należy podać algorytm, który zwróci 
długość najkrótszego cyklu w grafie. Należy podać rozwiązania dla grafów rzadkich i 
gęstych. Algorytm powinien stwierdzić, jeśli graf nie ma cyklu. Hint: w ani jedynm, ani 
drugim przypadku nie uda się uzyskać algorytmu liniowego. 
 """
""" 
1. ... (Nagranie)

1. Rozw dla grafow rzadkich:
    W sposob banalny usuwamy krawedz (x,y) i puszczamy algorytm Dijkstry z y do x, do otrzymanej odleglosci dodajemy wage krawedzi w(x,y)

 """