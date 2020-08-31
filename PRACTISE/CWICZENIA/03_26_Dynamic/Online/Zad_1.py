""" 
Zadanie 1. (problem sumy podzbioru)Dana jest tablicanliczbA. Proszę podać i zaimplementowaćalgorytm, który sprawdza, czy da się wybrać podciąg liczb zA, które sumują się do zadanej wartości T
 """

""" 
if tab[i]==j => f(i,j)=1, else f(i,j)=0
for i in (1,n):
    f(i,j)=max(f(i,j),f(i-1,j),f(i-1,(j-tab[i]) = 0 if <0))
--> O(n^2)
 """
