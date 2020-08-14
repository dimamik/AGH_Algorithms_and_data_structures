import sys
def sherlockAndMinimax(arr, p, q):
    a = arr[:]
    a.sort()
    best_diff = best_mid = 0
    for i in range(len(a) - 1):
        diff = a[i + 1] - a[i]
        mid = a[i] + int(diff / 2)
        if p <= mid <= q and diff > best_diff:
            best_diff = diff
            best_mid = a[i] + int(diff / 2)
    best_p = sys.maxsize
    best_q = sys.maxsize
    for v in a:
        diff_p = abs(v - p)
        diff_q = abs(v - q)
        if diff_p < best_p:
            best_p = diff_p
        if diff_q < best_q:
            best_q = diff_q
            
    best = best_mid
    if int(best_diff / 2) <= best_p:
        best = p
    if int(best_diff / 2) <= best_q and best_p < best_q:
        best = q
    return best
    

print(sherlockAndMinimax([46, 64, 26, 82, 18, 106, 60, 138, 194, 22], 82, 182))
