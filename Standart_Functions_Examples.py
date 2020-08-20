class Vertex():
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
    """ 
    Nadpisuje porownanie
     """
    def __lt__(self, value):
        return (self.value2<value.value2)

v = Vertex(5,2)
u = Vertex(1,3)
print(v>u)





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



