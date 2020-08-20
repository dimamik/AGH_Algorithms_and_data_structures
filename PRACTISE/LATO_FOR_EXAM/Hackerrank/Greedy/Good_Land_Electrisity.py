from tab import *

def pylons(k, arr):
    """ Будем путешествовать во времени 
        Расстояние между свечами должно быть меньше k"""
    i=k-1
    prev_index = 0
    tourches = [0] * len(arr)
    time = False
    while i<len(arr) and i>=0:
        if (arr[i]==1 and tourches[i]!=1):
            tourches[i]=1
            prev_index = i
            if (i+k>=len(arr)):
                time=True
            i+=2*(k-1)+1
            if (i>=len(arr) and not time):
                i=len(arr)-1
                time = True
        else:
            if (prev_index==i and not time):
                return -1
            i-=1
    c = 0
    for i in range(len(tourches)):
        if (tourches[i]==1):
            c+=1
    return c

print(pylons(4, tab))
