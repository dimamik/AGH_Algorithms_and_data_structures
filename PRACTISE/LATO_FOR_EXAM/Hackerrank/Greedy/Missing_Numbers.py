# Complete the missingNumbers function below.
def missingNumbers(brr, arr):
    arr = sorted(arr)
    brr = sorted(brr)
    to_ret = []
    b_c = 0
    for i in range(len(arr)):
        if (arr[i]!=brr[b_c]):
            b_c-=1
            to_ret.append(arr[i])
        b_c+=1
    return to_ret

print(missingNumbers([203, 204, 205, 206, 207, 208, 203, 204, 205, 206] , [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]))