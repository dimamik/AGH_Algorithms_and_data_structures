""" https://www.hackerrank.com/challenges/journey-to-the-moon/problem """
from math import *
def n_po_k(n,k):
    return factorial(n)//(factorial(n-k)*factorial(k))

def ZasadaWlWyl(n,tab_of_teams):
    sum = n_po_k(n,2)
    for i in range(len(tab_of_teams)):
        sum-=(n_po_k(tab_of_teams[i],2))
    return sum

def journeyToMoon(n, astronaut):
    """ First of all I need to define wich astranaut is from wich country """

    """ Doing it using hash table """
    if (len(astronaut)==0):
        return n_po_k(n,2)
    sets = []
    first_country = set()
    first_country.add(astronaut[0][0])
    first_country.add(astronaut[0][1])
    sets.append(first_country)
    for i in range(1,len(astronaut)):
        for j in range(len(sets)):
            if (sets[j].intersection(astronaut[i])):
                x = sets[j].intersection(astronaut[i])
                sets[j] = sets[j].symmetric_difference(astronaut[i])
                sets[j].update(sets[j],x)
            else:
                sets.append(set(astronaut[i]))
    """ Check if any of the sets intersect """
    i=0
    while i <len(sets):
        j=0
        while j<len(sets):
            if (i!=j and (len(sets[i].intersection(sets[j]))!=0)):
                sets[i] = sets[i].union(sets[j])
                sets.remove(sets[j])
                j-=1
            j+=1
        i+=1

    tab_of_teams = []
    for i in range(len(sets)):
        tab_of_teams.append(len(sets[i]))

    return ZasadaWlWyl(n,tab_of_teams)


print(journeyToMoon(5,[[0,1],[2,3],[0,4]]))