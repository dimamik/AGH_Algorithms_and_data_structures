from queue import *
""" Kolejka FIFO """
Q=Queue()
Q.put(4)
Q.put(5)
#print(Q.get())

""" Kolejka LIFO """
Q=LifoQueue()
Q.put(4)
Q.put(5)
#print(Q.get())

""" Sorting with sort_function """
tab=[(0,2),(1,1),(1,0)]
def second_el(tab):
    return tab[1]
tab=sorted(tab,reverse=False,key=second_el)
""" print(tab) """

""" XD """



