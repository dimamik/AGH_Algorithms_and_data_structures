class Node:
    def __init__(self,id):
        self.id=id
        self.parent=self
        self.rank=0
def find_set(x):
    if x!=x.parent:
        x.parent=find_set(x.parent)
    return x.parent
def union(x,y):
    x=find_set(x)
    y=find_set(y)
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
def is_cykle(x,y):
    x=find_set(x)
    y=find_set(y)
    if (x==y):return 1
    else:
        return 0

x=Node(1)
y=Node(2)
z=Node(3)
union(x,y)
k=find_set(x)
print(k.id)

