# Complete the maxSubarray function below.
def maxSubarray(arr):
    """ First Task """
    max_sum = float("-inf")
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum+=arr[i]
        max_sum=max(max_sum,curr_sum)
        if (curr_sum< 0 ):
            curr_sum = 0
    """ Second task """
    sec_ret = 0
    for i in range(len(arr)):
        if arr[i]>0:
            sec_ret+=arr[i]
    if (sec_ret==0):
        sec_ret = max(arr)
    return max_sum,sec_ret

print(maxSubarray([-2, -3, -1, -4, -6]))