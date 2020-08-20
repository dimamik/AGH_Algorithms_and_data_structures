def marcsCakewalk(calorie):
    calorie = sorted(calorie,reverse=True)
    sum = 0
    for i in range(len(calorie)):
        sum+=2**i * calorie[i]
    return sum
print(marcsCakewalk([1,3,2]))