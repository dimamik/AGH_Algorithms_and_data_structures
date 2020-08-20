""" Jak zaimplementować kolejkę na dwóch stosach? """
""" 
Stos A=[]
Stos B=[]

put_in_queue() -> push(A) // Dodaje element do A
take_from_queue()-> 
1) Spawdzam czy B jest puste, jesli tak,to:
    1) robie pop(B)
2) Jak B jest puste, to:
    1) Robię pop(A) dla n-1 elementów
    2) Zwrazam ostatni element
    3) Robie dla kazdego z tych elementow (z grupy n-1 push na stos B)

    Złożoność:
1) put_in_queue -> O(1)
2) take_from_queue -> O(1) - złożoność zamortyzowana bo kosztuję O(n) raz na n push() (Gdy kopiujemy elementy z jednego na drugi)
 """