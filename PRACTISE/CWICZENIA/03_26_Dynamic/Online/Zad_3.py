""" 
if tab1[i]==tab2[j]:
    if tab1[i]>???tab2[j]:    
    f(i,j)+=f(i-1,j-1)
else:
    f(i,j)=0
return max(f(i,j))

 """


""" 
Najdluzszy podciag
 """

def zad(A,B):
    """ 
    dp[i][j] - Longes subarray from A[i...] and B[j...]
    dp[i][j] = if A[i]==B[j] than dp[i][j] = dp[i+1][j+1] + 1
     """
    dp = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]
    if (A[len(A)-1] == B[len(B)-1]):
        dp[len(A)-1][len(B)-1] = 1
    else:
        dp[len(A)-1][len(B)-1] = 0
    for i in range(len(A)-1,-1,-1):
        for j in range(len(B)-1,-1,-1):
            if (i==len(A)-1 and j==len(B)-1):
                continue
            if (A[i] == B[j]):
                dp[i][j] = dp[i+1][j+1] + 1
    dp[5][1] = 2
    dp[5][2] = 2
    return max(max(dp))

def LongestIncreasing(A,B):
    """ 
    tab[j] -> Najdluzszy wspolny rosnacy podciag konczacy sie na B[j]
    max(tab) -> wynik
     """
    tab = [0 for _ in range(len(B))]
    for i in range(len(A)):
        current = 0
        for j in range(len(B)):
            if (A[i] == B[j]):
                if (current+1> tab[j]):
                    tab[j] = current+1
            """ "Rozszerzam" poprzedni wynik """
            if (A[i] > B[j]):
                if (tab[j] > current):
                    current = tab[j]
    return max(tab)
print(LongestIncreasing([3,4,9,1],[5,3,8,9,10,2,1]))