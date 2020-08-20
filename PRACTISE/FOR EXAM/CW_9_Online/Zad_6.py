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
        self.d=-1
def BuildFromInc(tab):
    """ 
    Buduje z listy sÄ…siedstwa w postaci tablicy
    Lista sÄ…siedstwa tab
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
def BFS(tab_of_v,s,t):
    """ 
    Input s is an index of start poing
     """
    Q=Queue()
    tab_of_v[s].visited=True
    tab_of_v[s].d=0
    Q.put(s)
    while Q.size!=0:
        u=Q.pop()
        for v in tab_of_v[u].tab_index_incident:
            if not tab_of_v[v].visited:
                tab_of_v[v].parrent=u
                tab_of_v[v].visited=True
                tab_of_v[v].d=tab_of_v[u].d+1
                Q.put(v)
            else:
                if v==t:
                    return tab_of_v[v].d
def BFS_modified(tab_of_v,s,t,d):
    Q=Queue()
    tab_of_v[s].visited=True
    tab_of_v[s].d=0
    Q.put(s)
    c_t=0
    while Q.size!=0:
        u=Q.pop()
        for v in tab_of_v[u].tab_index_incident:
            if not tab_of_v[v].visited:
                tab_of_v[v].parrent=u
                tab_of_v[v].visited=True
                tab_of_v[v].d=tab_of_v[u].d+1
                if tab_of_v[v].d<=d:
                    Q.put(v)
            if v==t:
                c_t+=1
    return c_t

def PsucieSciezki(tab_v,s,t):
    min_d=BFS(tab_v,s,t)
    for i in range(len(tab_v)):
        tab_v[i].visited=False
    c_t=BFS_modified(tab_v,s,t,min_d)
    return c_t
tab_v=BuildFromInc([[1,2,3],[4],[3,4,5],[],[6],[6],[]])     
tab_v=BuildFromInc([[1],[2,3,4],[5],[5],[5],[]])         
print(PsucieSciezki(tab_v,0,5))

