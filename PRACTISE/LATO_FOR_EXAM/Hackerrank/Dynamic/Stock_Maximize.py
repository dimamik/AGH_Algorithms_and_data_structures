def stockmax(prices):
    """ 
    For each of the days we find the optimal sell day and add it to ret_sum
    O(n^2)
     """
    to_ret = 0
    for i in range(len(prices)):
        max_prise = 0
        for j in range(i,len(prices)):
            max_prise = max(max_prise,prices[j])
        to_ret += ( max_prise - prices[i])
    return to_ret

def stockmax(prices):
    """ 
    For each of the days we find the optimal sell day and add it to ret_sum
    O(n) 
    We have curr maximum and for each day we can't get more than that value
     """
    to_ret = 0
    curr_max_price = float("-inf")
    for i in range(len(prices)-1,-1,-1):
        curr_max_price = max(curr_max_price,prices[i])
        to_ret+= ( curr_max_price - prices[i])
    return to_ret

print(stockmax([1, 2, 100]))