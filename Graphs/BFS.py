from graph_lib import *
from Stack_Queue import *
""" 
Breadth first search algotirhm

 """
def BFS(G,s):
    Q=Queue()
    s.d=0
    s.visited=True
    s.parrent=None
    Q.put(s)
    while not Q.is_empty():
        u=Q.get()
        for v in u.Polacz_Wierzch_ms:
            if not v.visited:
                v.visited=True
                print(v)
                v.d=u.d+1
                v.parrent=u
                Q.put(v)

X=Input_MSGraph()
BFS(X,0)
    
