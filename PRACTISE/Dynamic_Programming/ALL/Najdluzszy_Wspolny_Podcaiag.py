#Dane A i B tablicy, znalec ich najdluzszy wspolny podciag
def podc(A,B,ea,eb):
    if ea==0 or eb==0:
        return 0
    if A[ea]==B[eb]:
        return 1+podc(A,B,ea-1,eb-1)
    else:
        return max(podc(A,B,ea-1,eb),podc(A,B,ea,eb-1))+1

# Dynamic Programming implementation of LCS problem 

def lcs(X , Y): 
	# find the length of the strings 
	m = len(X) 
	n = len(Y) 
	# declaring the array for storing the dp values 
	L = [[None]*(n+1) for i in range(m+1)] 
 

	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j] , L[i][j-1]) 
 
	return L[m][n] 

print(podc([1,3,73,4],[1,3,72,4],3,3))
    