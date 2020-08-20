""" Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter. """
from datetime import datetime
import time
start_time = datetime.now()
inf = float('inf')
_inf = float('-inf')
def Recursiv_Coin(tab_of_coins,val):
    if val<tab_of_coins[0]: return 99999
    for i in range(len(tab_of_coins)):
        if tab_of_coins[i]==val:return 1
    q=99999
    for i in range(len(tab_of_coins)):
        q=min(q,1+Recursiv_Coin(tab_of_coins,val-tab_of_coins[i]))
    return q

#print(Recursiv_Coin([1,2,5],150))
def Non_Recursive_Coin(tab_of_coins,tab_f,val):
    if val<len(tab_f) and tab_f[val]>0:
        return tab_f[val]
    if val<tab_of_coins[0]: return 99999
    for i in range(len(tab_of_coins)):
        if tab_of_coins[i]==val:
            tab_f[val]=1
            return 1 
    q=inf
    for i in range(len(tab_of_coins)):
        q=min(q,1+Non_Recursive_Coin(tab_of_coins,tab_f,val-tab_of_coins[i]))
    tab_f[val]=q
    return q
    
def Bottom_Up_Coint(tab_of_coins,val):
    tab_f=[0]*max(tab_of_coins[len(tab_of_coins)-1],(val+1))
    for i in range(len(tab_of_coins)):
        tab_f[tab_of_coins[i]]=1
    for i in range(0,val+1):
        q=inf
        for j in tab_of_coins:
            if j<=i:
                q=min(q,1+tab_f[i-j])
                tab_f[i]=q
            else:break
        
    return tab_f[val]
print(Bottom_Up_Coint([1,2,5,10,20,50],1500000))        

    
    


#print(Non_Recursive_Coin([1,2,5,10,20,50],[0]*1500001,1500000))
print(datetime.now() - start_time)
    