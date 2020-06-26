def Koszt(A,B):
    if len(A[0])!=len(B):
        raise "ROZNE DLUGOSCI"
    return len(A)*len(A[0])*len(B[0])

def MinKost(tab):
    F=[float("inf")]*len(tab)
    for i in range(len(tab)):
        F[i]=[float("inf")]*len(tab)
    for i in range(len(tab)):
        F[i][i]=0
    for i in range(len(tab)-1):
        F[i][i+1]=Koszt(tab[i],tab[i+1])
    print("LOL")
    for i in range(len(tab)):
        for j in  range(len(tab)):
            for k in range(i,j):
                koszt=(len(tab[i])*len(tab[k][0])*len(tab[j][0]))
                F[i][j]=min(F[i][j],F[i][k]+F[k+1][j]+koszt)
    print(F)

print(MinKost([[[1,1],[2,2],[3,3]],[[1,1,3,5,1],[7,15,12,23,5]],[[1,7,8,9,4,5],[1,1,1,1,1,1],[1,7,8,9,4,5],[1,7,8,9,4,5],[1,7,8,9,4,5]]]))
