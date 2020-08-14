from zad2testy import runtests

""" Dzmitry Mikialevich """

""" Algorytm jest podobny do mnożenie macierzy 
Ale znacznie trudniejszy ...
"""

def opt_sum(tab):
    """ 
    F[i][j] -> Największy co do wartosci bezwzglednej wynik tymczasowy między [i,j]
    S[i][j] -> Summa z tab od [i,j]
     """
    F = [float("inf")]*len(tab)
    P = [float("inf")]*len(tab)
    S = [0]*len(tab)
    for i in range(len(tab)):
        F[i] = [float("inf")]*len(tab)
        P[i] = [float("inf")]*len(tab)
        S[i] = [0]*len(tab)
    for i in range(len(tab)):
        S[i][i] = tab[i]
    for i in range(0, len(tab)):
        for j in range(i+1, len(tab)):
            S[i][j] = S[i][j-1] + tab[j]

    for i in range(len(tab)):
        for j in range(i, len(tab)):
            if (i == j):
                F[i][j] = 0
            elif (abs(i-j) == 1):
                F[i][j] = abs(tab[j] + tab[i])

    for i in range(len(tab)):
        for j in range(len(tab)):
            for k in range(i,j):
                """ группировка по k """
                koszt = abs(S[i][k] + S[k+1][j])
                F[i][j] = min(F[i][j], max(F[i][k], F[k+1][j], koszt))
                """ F[i][j]=min(F[i][j],new_val) """
                """ if F[i][j]>new_val:
                    F[i][j]=new_val
                    P[i][j]=k """

    return (F[0][len(tab)-1])


opt_sum([3, 2, -3, 4, 5, -9])
runtests( opt_sum )
