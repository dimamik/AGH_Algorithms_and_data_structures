def Fibb(x):
    """ 
    Program wypisze ciąg Fibbonaciego
     """
    tab=[0]*x
    tab[0]=1
    tab[1]=1
    print(1,1)
    for i in range(2,x):
        tab[i]=tab[i-1]+tab[i-2]
        print(tab[i])

Fibb(15)
def printrec(tab,P,i):
    if i>=0:
        printrec(tab,P,P[i])
        print(tab[i])

def NajdluzszyPodciagRosnacy(tab):
    F = [1]*len(tab)
    P=[-1]*len(tab)
    F[0]=1
    for i in range(1,len(tab)):
        """ 
        Finding max from previous
         """
        for j in range(i):
            if tab[j]<tab[i] and F[i]<F[j]+1:
                F[i]=F[j]+1
                P[i]=j
    max_el_index=0
    for i in range(len(F)):
        if F[i]>F[max_el_index]:
            max_el_index=i
    
    print(P)
    printrec(tab,P,max_el_index)

NajdluzszyPodciagRosnacy([3,1,5,7,2,4,1,15])

