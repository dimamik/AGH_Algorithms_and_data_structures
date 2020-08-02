def maximumGap(self, num):
        if len(num) < 2 or min(num) == max(num):
            return 0
        a, b = min(num), max(num)
        size = (b-a)//(len(num)-1) or 1
        bucket = [[None, None] for _ in range((b-a)//size+1)]
        for n in num:
            b = bucket[(n-a)//size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(bucket[i][0]-bucket[i-1][1] for i in range(1, len(bucket)))

def zad7(tab):
    min_el=min(tab)
    max_el=max(tab)
    rozd_Bucketa=max_el/len(tab)
    n=len(tab)
    Buckets=[[] for _ in range(n+1)]
    for number in tab:
        index_of_Bucket=int (number/rozd_Bucketa)
        #add using insertion sort in bucket (but in this case just add)
        Buckets[index_of_Bucket].append(number)
    for i in range(n+1):
        if Buckets[i]!=[]:
            min_in_b=min(Buckets[i])
            max_in_b=max(Buckets[i])
        else:
            max_in_b=0
            min_in_b=0
        Buckets[i]=[min_in_b,max_in_b]
    i=0
    """ while i<len(Buckets):
        if Buckets[i][1]==0:
            Buckets.pop(i)
        i+=1 """
    """ print(Buckets) """
    max_rozn=-1
    for i in range(len(Buckets)-1):
        max_rozn=max(max_rozn,abs(Buckets[i+1][0]-Buckets[i][1]))
    """ print(max_rozn) """
    return max_rozn

""" zad7([40,31,62,72,7,19,30,86,15]) """
from random import *
def Checker(x):
    for i in range(x):
        l=randint(1,999)
        tab=[]
        for i in range(l):
            tab.append(randint(0,999))
        G=maximumGap
        if zad7(tab)==maximumGap(G,tab):
            print("OK")
        else:

            print("NOT OK\n",zad7(tab),maximumGap(G,tab))

Checker(10)
        


    