#Masz dlugosc pretu (n) i ceny kazdej dlugosci mozliwego kawalku, return MaxUzyskamy
#F.e 
#Naive solution
def Pret_Rec(price,curr_len):
    if curr_len==0:return 0
    q=-9999
    for  i in range(1,curr_len+1):
        q =max(q,price[i]+Pret_Rec(price,curr_len-i))
    return q


def Pret_Rec_2(price,curr_len,r):
    if r[curr_len]>=0: return r[curr_len]
    if curr_len==0:return 0
    q=-9999
    for  i in range(1,curr_len+1):
        q =max(q,price[i]+Pret_Rec(price,curr_len-i))
    r[curr_len]=q
    return q

def F(price,n):
    r=[-1]*(n+1)
    r[0]=0
    r[1]=price[1]
    for i in range(1,n+1):
        Pret_Rec_2(price,i,r)
    return r[n]


import time
import random
start = time.process_time()
#
tab = [random.randint(1,50) for _ in range(40)]
print(random.randint(1,50) for _ in range(40))
print(time.process_time() - start)


