def maxMin(k, arr):
    arr = sorted(arr)
    min_sum = float("inf")
    step = 0
    for step in range(len(arr)-k+1):
        min_sum = min(min_sum, arr[k-1 + step] - arr[0 +step ])
    return min_sum
    
tab =[4504,
1520,
5857,
4094,
4157,
3902,
822,
6643,
2422,
7288,
8245,
9948,
2822,
1784,
7802,
3142,
9739,
5629,
5413,
7232]
tab2 = [
    7,
3,
100,
200,
300,
350,
400,
401,
402
]
print(maxMin(3 , tab2))
tab1 =[2,1,2,1,2,1]