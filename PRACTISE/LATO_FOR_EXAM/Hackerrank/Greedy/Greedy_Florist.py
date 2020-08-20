# Complete the getMinimumCost function below.
def getMinimumCost(k, tab):
    tab = sorted(tab,reverse = True)
    c,sum,delta,i = 0,0,1,0
    while i < len(tab):
        if (c<k):
            c+=1
            sum+=(delta*tab[i])
        else:
            delta+=1
            c=1
            sum+=(delta*tab[i])
        i+=1
    return sum


print(getMinimumCost(2 , [2, 5, 6]))