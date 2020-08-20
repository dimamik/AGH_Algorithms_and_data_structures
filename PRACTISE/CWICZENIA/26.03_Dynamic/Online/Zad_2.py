""" 
Mamy dane dwie tablice,A[n] iB[n]. Należy znaleźć długośćich najdłuższego wspólnego podciągu. (Klasyczny algorytm dynamicznyO(n2))
 """
""" 

if tab1[i]==tab2[j]:
    f(i,j)+=f(i-1,j-1)
else:
    f(i,j)=0
return max(f(i,j))

 """