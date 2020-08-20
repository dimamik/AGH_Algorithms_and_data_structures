def luckBalance(k, contests):
    contests=sorted(contests,reverse=True)
    luck = 0
    for i in range(len(contests)):
        if (contests[i][1] == 0):
            luck += contests[i][0]
        elif (k > 0):
            k -= 1
            luck += contests[i][0]
        else:
            luck -= contests[i][0]
    return luck


print(luckBalance(3, [
    [5, 1],
    [2, 1],
    [1, 1],
    [8, 1],
    [10, 0],
    [5, 0]]))
