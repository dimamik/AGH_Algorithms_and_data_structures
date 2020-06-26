def zad(A,B):
    n=len(A)
    tab=[0]*len(A)
    for i in range(n):
        tab[i]=[0]*len(A)
    print(tab[n-1][n-1])
    """ tab[0][0]=5 """
    for i in range(0,n):
        for j in range(0,n):
            if A[i]==B[j]:
                val=tab[i-1][j-1]
                if j-1<0 or i-1<0:
                    val=0
                tab[i][j]=val+1
            else:
                tab[i][j]=max(tab[i-1][j],tab[i][j-1])
    print(tab)

""" zad([1,3,5,8,9],[1,2,4,3,9]) """
zad([2,0,5,7,9,15,3,8],[0,5,2,9,3,1,1,1])