def Koszt(A,B):
    if len(A[0])!=len(B):
        raise "ROZNE DLUGOSCI"
    return len(A)*len(A[0])*len(B[0])

def MinKost(tab):
    F=[float("inf")]*len(tab)
    P=[float("inf")]*len(tab)
    for i in range(len(tab)):
        F[i]=[float("inf")]*len(tab)
        P[i]=[float("inf")]*len(tab)   
    for i in range(len(tab)):
        F[i][i]=0
    for i in range(len(tab)-1):
        F[i][i+1]=Koszt(tab[i],tab[i+1])
    for i in range(len(tab)):
        for j in  range(len(tab)):
            for k in range(i,j):
                koszt=(len(tab[i])*len(tab[k][0])*len(tab[j][0]))
                new_val=F[i][k]+F[k+1][j]+koszt
                """ F[i][j]=min(F[i][j],new_val) """
                if F[i][j]>new_val:
                    F[i][j]=new_val
                    P[i][j]=k
    print(P)
    BracketConvertor(P)
    return F[0][len(tab)-1]
from random import *
def BracketConvertor(P):
    string=[None]*len(P)
    for i in range(len(P)):
        x=i
        string[i]=str(x)
    for i in range(len(P)):
        for j in range(len(P)):
            if P[i][j]!=float("inf"):
                k=P[i][j]
                f="("+string[i]
                string[i]=f
                string[k]+=")" 
    print(string)

def MatrixConverter(tab):
    to_ret=[]
    for i in range(len(tab)):
        M1=[None]*tab[i][0]
        for j in range(tab[i][0]):
            M1[j]=[randint(0,999)]*tab[i][1]
        to_ret.append(M1)
    """ print(to_ret) """
    return to_ret
        

x=MatrixConverter([[20,15],[15,3],[3,20],[20,1],[1,7]])
print(MinKost(x))
""" print(MinKost([[[1,1],[2,2],[3,3]],[[1,1,3,5,1],[7,15,12,23,5]],[[1,7,8,9,4,5],[1,1,1,1,1,1],[1,7,8,9,4,5],[1,7,8,9,4,5],[1,7,8,9,4,5]]])) """
