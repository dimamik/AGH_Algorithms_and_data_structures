import math
import os
import random
import re
import sys
class Vertex():
    def __init__(self,id):
        """ 
        Inicialization is equivalent to operation make_set()
         """
        self.id=id
        self.parent_in_union=self
        self.rank_of_union=0
        self.parrent=-1
        self.color=-1
        self.tab_index_incident=[]
        self.visited=False
        self.entry=-1
        self.process=-1
class PseudoVertex():
    """ 
    Pomocnicza klasa dla przechowywania wag
     """
    def __init__(self,index=-1,waga=-1):
        self.index=index
        self.waga=waga
def BuildTab_of_v(tab,n,skierowany=False):
    """ 
    n - ilosc wierzcholkow (licząc od 0)
    [u,v,w] ->wierzcholek z u do v o wadze w
    takes tab=[[0,2,3],...[]]
     """
    tab_of_v=[None]*n
    for i in range(n):
        tab_of_v[i]=Vertex(i)
    for i in range(len(tab)):
        (tab_of_v[tab[i][0]].tab_index_incident).append(PseudoVertex(tab[i][1],tab[i][2])
        )
        if not skierowany:
            (tab_of_v[tab[i][1]].tab_index_incident).append(PseudoVertex(tab[i][0],tab[i][2])
        )
    return tab_of_v

def find_set(x):
    if x!=x.parent_in_union:
        x.parent_in_union=find_set(x.parent_in_union)
    return x.parent_in_union
def union(x,y):
    x=find_set(x)
    y=find_set(y)
    if x.rank_of_union>y.rank_of_union:
        y.parent_in_union=x
    else:
        x.parent_in_union=y
        if x.rank_of_union==y.rank_of_union:
            y.rank_of_union+=1
def is_cykle(x,y):
    x=find_set(x)
    y=find_set(y)
    if (x==y):return 1
    else:
        return 0

""" x=Vertex(1)
y=Vertex(2)
z=Vertex(3)
union(x,y)
k=find_set(x)
print(k.id) """

def Kruskal(tab_of_v):
    """ Posortuj krawędzie rosnąco według wag """
    tab_of_edges=[]
    for i in range(len(tab_of_v)):
        for j in range(len(tab_of_v[i].tab_index_incident)):
            w=tab_of_v[i].tab_index_incident[j].waga
            ind=tab_of_v[i].tab_index_incident[j].index
            tab_of_edges.append((w,i,ind))
    tab_of_edges=sorted(tab_of_edges)
    MST=[]
    for i in range(len(tab_of_edges)):
        if find_set(tab_of_v[tab_of_edges[i][1]])!=find_set(tab_of_v[tab_of_edges[i][2]]):
            MST.append((tab_of_edges[i][1],tab_of_edges[i][2]))
            union(tab_of_v[tab_of_edges[i][1]],tab_of_v[tab_of_edges[i][2]])
    print(MST)
    """ 
    ZWRACA W POSTACI SKIEROWANEJ ALE TRAKTUJEMY JAKO NIESKIEROWANE
     """
    #print(tab_of_edges)
    return MST

def zad(n, k, roads):
    g = BuildTab_of_v(roads,n+1)
    MST = Kruskal(g)
    pass



# print(zad(5, 3, [[1, 2, 1], [2, 3, 2], [2, 4, 2], [3, 5, 3]]))


