# Complete the cost function below.
def cost(B):
    F = [[0]*2 for _ in range(len(B))]
    for i in range(1, len(B)):
        for j in range(2):
            if (j == 0):
                F[i][j] = max(F[i-1][0] + abs(B[i]-B[i-1]),
                              F[i-1][1] + abs(B[i]-1))
                pass
            else:
                F[i][j] = max(F[i-1][0] + abs(1-B[i-1]),
                              F[i-1][1])
                pass
    return max(F[len(B)-1][0], F[len(B)-1][1])


print(cost([100, 2, 100, 2, 100]))
