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
def print_unions(tab_of_unions):
    """ 
    takes a tab_of_unions[n] where tab_of_unions[i] is Node()
    and makes a dictionary from it with a values inside dictionary
     """
    tab_to_ret = []
    dic = dict()
    for i in range(1,len(tab_of_unions)):
        parent = find_set(tab_of_unions[i]).id
        if parent in dic:
            dic[parent].append(tab_of_unions[i].id)
        else:
            dic[parent] = [tab_of_unions[i].id]
    print(dic)
    return dic

x=Node(1)
y=Node(2)
z=Node(3)
union(x,y)
k=find_set(x)
print(k.id)

