""" https://www.hackerrank.com/challenges/wet-shark-and-two-subsequences/problem """
import pprint
def twoSubsequences(x, r, s):
    mod=1e+7
    """ f(i,j,k) -> the  number of subsets """
    F = [[[0 for k in range(len(x))] for j in range(len(x))] for i in range((r+s)//2 +1)]
    pprint.pprint(F)
    F[0][0][0]=1
    for i in range(1,len(x)):
        for j in range(len(x)):
            for k in range(r+s//2):
                F[i][j][k] =F[i-1][j][k]
                if (x[i] <=j and k>=1): F[i][j][k]+=F[i-1][j-1][k-x[i]]
                F[i][j][k]%=mod
    to_ret = 0
    for i in range(1,len(x)):
        to_ret+=F[len(x)-1][i][(r+s)//2] *F[len(x)-1][i][(r-s)//2] 
        to_ret%=mod
    return to_ret
    pass
twoSubsequences([1,1,1,4],5,3)