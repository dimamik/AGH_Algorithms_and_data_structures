""" https://www.hackerrank.com/challenges/fibonacci-modified/problem """
def fibonacciModified(t1, t2, n):
    if (n==1):
        return t1
    if (n==2):
        return t2
    """ The point is to collect on the stack last two values """
    a_i_prev = t2
    a_i_pprev = t1
    curr = t2
    for _ in range(n-2):
        curr = (a_i_prev)**2 + a_i_pprev
        a_i_pprev = a_i_prev
        a_i_prev = curr
    return curr

print(fibonacciModified(0,1,5))

