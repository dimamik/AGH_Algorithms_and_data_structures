from random import *
def CoinChange(coins,k):
    coins = sorted(coins,reverse = True)
    curr = 0
    sum = 0
    while (k>0 and curr<len(coins)):
        if (k-coins[curr]>=0):
            k-=coins[curr]
            sum+=1
        else:
            curr+=1
    return sum



tab_coins = [1,2,5,10,50,100,200,500]
x = randint(1e2,1e5)
print(x)
print(CoinChange(tab_coins,x))