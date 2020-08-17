""" https://www.hackerrank.com/challenges/coin-change/forum """


def getWays(n, coins):
    coins.sort()
    """ F[i][k] - Ways of exchanging i$ using coins from [0,k]
    F[0][0,len] = 0
    F[c[0]][0,len] = 1
    F[i][k] = F[i-c[k]][k] +(F[c[k]][k] - F[c[k]-1][k])+ F[i][k-1] function =0 when parametrs go beyond 0
     """
    F = [[0]*(len(coins)) for _ in range(n+1)]
    print(F)
    for i in range(len(coins)):
        F[0][i]=1
    for i in range(n+1):
        if (i==0 or i%coins[0]==0):
            F[i][0] = 1
    for dollars in range(1,n+1):
        for coin in range(1,len(coins)):
            first_to_add = 0
            second_to_add = 0
            if (dollars - coins[coin] >=0 and coin >= 0):
                first_to_add=F[dollars - coins[coin]][coin]
            if (coin-1 >=0):
                second_to_add = F[dollars][coin-1]
            F[dollars][coin] = first_to_add+second_to_add
    return F[n][len(coins)-1]



def getWays1(n, c):
    # Complete this function
    n_perms = [1]+[0]*n
    for coin in c:
        for i in range(coin, n+1):
            n_perms[i] += n_perms[i-coin]
    return n_perms[n]
    
print(getWays1(10 ,[2, 5, 3, 6]))