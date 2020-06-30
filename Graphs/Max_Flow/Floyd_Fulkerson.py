def ZbudujSiecResidualną(G,P):
    """ Budowanie sieci residualnej """
    R=[None]*len(G)
    for i in range(len(G)):
        R[i]=[-1]*len(G)
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0:
                R[i][j]=G[i][j]
                R[j][i]=P[i][j]
                if R[j][i]==0:
                    R[j][i]=-1
                if R[i][j]==0:
                    R[i][j]=-1
    return R

def Sciezka_Powieksz(R,s,t):
    Q=[]
    tab_d=[float("inf")]*len(R)
    tab_p=[-1]* len(R)
    tab_v = [False] * len(R)
    tab_v[s]=True
    tab_d[s]=0
    Q.append(s)
    while len(Q)>0:
        u=Q.pop()
        for v in range(len(R)):
            if R[u][v]!=-1 and not tab_v[v]:
                tab_v[v]=True
                tab_d[v]=tab_d[u]+1
                tab_p[v]=u
                Q.append(v)
    min_flow=999
    u=tab_p[t]
    v=t
    while u!=-1:
        min_flow=min(R[u][v],min_flow)
        v=u
        u=tab_p[v]

    if min_flow>100:
        min_flow=-1
    return min_flow,tab_p




def zad(G,s,t):
    """ 
    G - graf pojemnosci w postaci macierzy incydencji
     """
    P = [None]*len(G)
    for i in range(len(G)):
        P[i]=[0] * len(G)
    
    """ Znajdz sciezke powiekszajaca w sieci residualnej """
    max_flow=0
    R=ZbudujSiecResidualną(G,P)
    min_c_flow,tab_p=Sciezka_Powieksz(R,s,t)
    while min_c_flow>0:
        """ Rysuje droge przeplywu """
        u=tab_p[t]
        v=t
        output=[]
        while u!=-1:
            """ print("(",u,"->",v,")", end=" ") """
            output.append((u,v))
            v=u
            u=tab_p[v] 
        """ print(min_c_flow) """
        output=sorted(output)
        output.append(' Płynie -> ')
        output.append(min_c_flow)
        print(output)


        max_flow+=min_c_flow
        u=tab_p[t]
        v=t
        while u!=-1:
            G[u][v]-=min_c_flow
            P[u][v]+=min_c_flow
            v=u
            u=tab_p[v]
        R=ZbudujSiecResidualną(G,P)
        min_c_flow,tab_p=Sciezka_Powieksz(R,s,t)
    return max_flow


    
tab_v=[
    [0,4,3,0,0,0],
    [0,0,2,2,0,0],
    [0,0,0,2,2,0],
    [0,0,0,0,0,4],
    [0,0,0,0,0,5],
    [0,0,0,0,0,0]
]
print(zad(tab_v,0,5))


    