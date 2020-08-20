


""" 
ROZWIĄZANIE by anetaporebska:

W pierwszej kolejności zamieniam literę a na 0, a literę b na 1.                                                                    O(n)
Teraz kążdemu podciągowi będę mogła przypisać liczbę dziesiętną - np. bab (101) = 5                                                 
Tworzę nową tablicę w której będę gromadzić przypisane ciągom liczby dziesiętne, jej długość to (n-k+1), bo tyle maksymalnie        O(n)
mogę mieć różnych wartości.
Liniowo iteruję po ciągu n liter i dodaję liczby dziesiętne odpowiadające każdemu podciągowi do poprzednio utworzonej               O(n)
tablicy.
Sortuję zawartość tej tablicy używając bucket sort, ponieważ mogę założyć że wartości są rozłożone jednostajnie.                    O(n)
(uwaga: dla bardzo małych k=1,2,3 bardziej opłaca się użyć counting sorta)
Na samym końcu iteruję po już posortowanej tablicy szukając najczęściej występującej liczby (zapamiętując counter i wartosć)        O(n)
Otrzymaną wartośc zamieniam na liczbę binarną a następnie na ciąg liter i zwracam jako wynik.                                       O(1)

Złożonośc:
5*O(N)+O(1)=O(N)

 """