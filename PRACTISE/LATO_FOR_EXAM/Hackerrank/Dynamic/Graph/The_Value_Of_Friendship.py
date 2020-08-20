class Node:
    """ Node of Union """
    def __init__(self,id):
        self.id=id
        self.parent=self
        self.rank=0
        self.size = 0
def find_set(x):
    if x!=x.parent:
        x.parent=find_set(x.parent)
    return x.parent
def union(x,y):
    x=find_set(x)
    x.size+=1
    y=find_set(y)
    y.size+=1
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1



def count_unions(tab_of_unions):
    tab_to_ret = []
    dic = dict()
    for i in range(1,len(tab_of_unions)):
        parent = find_set(tab_of_unions[i]).id
        if parent in dic:
            dic[parent].append(tab_of_unions[i].id)
        else:
            dic[parent] = [tab_of_unions[i].id]
    sum = 0
    for value in dic.values():
        sum+=(len(value) * (len(value)-1))
    return sum
def valueOfFriendsship(n, friendships):
    for i in range(len(friendships)):
        friendships[i].sort()
    friendships.sort()
    """ Unii """
    tab_unions = [None] * (n+1)
    for i in range(1,n+1):
        tab_unions[i] = Node(i)
    sum = 0
    for fr,sr in friendships:
        union(tab_unions[fr],tab_unions[sr])
        sum+=count_unions(tab_unions)
    return sum

print(valueOfFriendsship(4,[[1, 2], [3, 2], [4, 2], [4, 3]]))
