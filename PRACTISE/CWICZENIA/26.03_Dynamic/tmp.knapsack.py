def KnapSack(weight,val,MaxWeight):
    tab=[None]*len(val)
    for i in range(len(val)):
        tab[i]=[0]*(MaxWeight+1)
    for i in range(weight[0],MaxWeight+1):
        tab[0][i]=val[0]
    for i in range(1,len(val)):

        for j in range(1,MaxWeight+1):
            tab[i][j]=tab[i-1][j]
            if j>=weight[i]:
                tab[i][j]=max(tab[i][j],tab[i-1][j-weight[i]]+val[i])
    return tab
#Returning the indexes of values we take
def print_items(weight,val,MaxWeight):
    tab = KnapSack(weight,val,MaxWeight)
    tab_to_ret = []
    curr_weight=MaxWeight
    print(curr_weight)
    for i in range(len(val)-1,0,-1):
        prev_val=tab[i-1][curr_weight]
        curr_val=tab[i][curr_weight]
        if curr_val>prev_val:
            tab_to_ret.append(i)
            curr_weight-=weight[i]
    return tab_to_ret


print(print_items([1,3,4,5],[1,4,5,7],7))
    
