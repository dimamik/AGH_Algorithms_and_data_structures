""" Dana jest tablica n liczb A. Czy da sie wybrac podciag sumuvacy sie do podanev wartosci """
def podc(tab,i,v):
    if v==tab[i]:return 1
    if i<0:return 0
    if i==0 and v==tab[0]:return 1
    #if v in tab:return 1
    return max(podc(tab,i-1,v),podc(tab,(i-1),(v-tab[i])))
def podc_Non_Recursive(tab,v):
    tab_f = [[[-1] for i in range(len(tab))] for i in range(0,v+1)] 
    for i in range(len(tab)):
        for j in range(len(tab)):
            tab_f[tab[i]][j]=1
    for i in range(len(tab)):
        tab_f[0][i]=1
    
    for j in range(v+1):
        for i in range(len(tab)):
            if tab_f[j][i]==-1:
                if i-1<0:break
                tab_f[j][i]=max(tab_f[j-1][i],tab_f[v-tab[i],i-1])
    print(tab_f)
print(podc_Non_Recursive([1,4,3,5],20))

