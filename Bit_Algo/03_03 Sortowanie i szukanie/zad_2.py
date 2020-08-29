def zad(tab):
    sum = 0
    curr_el = 0
    for i in range(len(tab)):
        if (tab[i] == 0):
            sum+=2*(i-curr_el)
            curr_el+=1
    return sum
print(zad([0,1,1,0,1,0,1,1,0,1,0,0]))