# Complete the candies function below.
def candies(n, arr):
    tmp_arr = [0] * len(arr)
    for i in range(len(arr)):
        tmp_arr[i] = arr[i]
    for i in range(len(arr)):
        arr[i] = [arr[i],i]
    arr = sorted(arr)
    arr_candies = [0] * len(arr)
    for i in range(len(arr)):
        """ Choose max from neighbours """
        index = arr[i][1]
        n1 = index-1
        n2 = index+1
        max_val = 0
        if (n1>=0 and arr[i][0]>tmp_arr[n1]):
            max_val=max(arr_candies[n1],max_val)
        if (n2<len(arr)and arr[i][0]>tmp_arr[n2]):
            max_val = max(arr_candies[n2],max_val)
        arr_candies[index] = max_val+1
    sum = 0
    for i in range(len(arr_candies)):
        sum+=arr_candies[i]
    return sum         

candies(3 , [1, 2, 2])