""" https://www.hackerrank.com/challenges/board-cutting/problem """

# Complete the boardCutting function below.
def boardCutting(cost_y, cost_x):
    mod  = (10**9 + 7)
    costs = []
    for i in range(len(cost_y)):
        costs.append([cost_y[i],i,0])
    for i in range(len(cost_x)):
        costs.append([cost_x[i],i,1])
    costs = sorted(costs,reverse = True)
    horizontal = 1
    vertical = 1
    sum = 0
    for  i in range(len(costs)):
        if (costs[i][2]==0):
            """ Horizontal """
            sum+=costs[i][0] * vertical
            horizontal+=1
            pass
        else:  
            sum+=costs[i][0] * horizontal
            vertical+=1
    return sum % mod

boardCutting([2, 1, 3, 1, 4] , [4, 1, 2])
