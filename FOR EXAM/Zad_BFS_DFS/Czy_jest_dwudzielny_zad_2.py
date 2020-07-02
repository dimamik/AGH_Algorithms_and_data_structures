class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None
class Queue():
    """ 
    Classic Queue on lists based on VALUE
     """
    def __init__(self):
        self.first=None
        self.last=self.first
        self.size=0
    def is_empty(self):
        return self.size==0
    def pop(self):
        """ 
        Gives the first element in the queue
         """
        if self.size==0:
            raise "size=0"
        self.size-=1
        if self.first.next!=None:
            to_ret=self.first.val
            self.first=self.first.next
            return to_ret
        else:
            tmp=self.first.val
            self.first=None
            self.last=None
            return tmp
    def put(self,val):
        """ 
        Puts value in the end of the queue
         """
        tmp=Node(val)
        self.size+=1
        if self.last==None:
            self.first=tmp
            self.last=self.first
            
        else:
            self.last.next=tmp
            self.last=tmp
""" 
TEST QUEUE
Q= Queue()
Q.put(45)
Q.put(15)
Q.put(10)
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop()) 
"""
class Vertex():
    """ 
    The way of using:
    [x,y,z], x-veris
     """
    def __init__(self):
        self.parrent=-1
        self.color=-1
        self.tab_index_incident=None
        self.visited=False
def BuildFromInc(tab):
    """ 
    Buduje z listy sąsiedstwa w postaci tablicy
    Lista sąsiedstwa tab
    tab=[[2,3],[1,5],...]
     """
    tab_of_v=[None]*len(tab)
    for i in range(len(tab)):
        V=Vertex()
        V.tab_index_incident=tab[i]
        tab_of_v[i]=V
    return tab_of_v
""" 
Test of BuildFromInc
BuildFromInc([[1],[2],[]]) """
def CzyJestDwudzielny(tab_of_v,s):
    """ 
    Input s is an index of start poing
     """
    Q=Queue()
    tab_of_v[s].color=0
    tab_of_v[s].visited=True
    Q.put(s)
    while Q.size!=0:
        u=Q.pop()
        for v in tab_of_v[u].tab_index_incident:
            if v==tab_of_v[u].parrent:
                continue
            """ v - index of connected vertex """
            if not tab_of_v[v].visited:
                tab_of_v[v].parrent=u
                tab_of_v[v].visited=True
                if tab_of_v[u].color==1:
                    tab_of_v[v].color=0
                else:
                    tab_of_v[v].color=1
                Q.put(v)
            else:
                if tab_of_v[v].color==tab_of_v[u].color:
                    return "Nie jest dwudzielny"
    return "Jest Dwudzielny"
    

"""     Test dla dwudzielnosci
tab_of_v=BuildFromInc([[1,3],[2,0],[1,3],[2,0]]) 
print(CzyJestDwudzielny(tab_of_v,0)) """

def CzyPosiadaCykl(tab_of_v,s):
    """ 
    Input s is an index of start poing
     """
    Q=Queue()
    tab_of_v[s].color=0
    tab_of_v[s].visited=True
    Q.put(s)
    while Q.size!=0:
        u=Q.pop()
        for v in tab_of_v[u].tab_index_incident:
            if v==tab_of_v[u].parrent:
                continue
            """ v - index of connected vertex """
            if not tab_of_v[v].visited:
                tab_of_v[v].parrent=u
                tab_of_v[v].visited=True
                if tab_of_v[u].color==1:
                    tab_of_v[v].color=0
                else:
                    tab_of_v[v].color=1
                Q.put(v)
            else:
                return "Posiada cykl"
    return "Nie posiada cyklu"

tab_of_v=BuildFromInc([[1],[2,0],[1,3],[2]]) 
print(CzyPosiadaCykl(tab_of_v,0))

    


    



