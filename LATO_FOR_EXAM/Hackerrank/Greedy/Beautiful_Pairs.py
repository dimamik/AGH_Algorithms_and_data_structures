# Complete the beautifulPairs function below.
from tab import *
def beautifulPairs(A, B):
    H = {}
    for i in range(len(A)):
        if str(A[i]) not in H:
            H[str(A[i])] = 1
        else:
            H[str(A[i])]+=1
    k = len(H)
    c=0
    to_add = -1
    for i in range(len(B)):
        if str(B[i]) in H and H[(str(B[i]))]!=0:
            H[(str(B[i]))] -=1
            c+=1
        else:
            to_add=1
    return (c+to_add)


print(beautifulPairs(tab,tab2))


