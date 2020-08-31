class Node():
    def __init__(self,val):
        self.val = val
        self.kids = []
        self.max_val = float("-inf")
    def __str__(self):
        return str(self.val)

def zad(root):
    """ 
    -> O(n), where n is the number of edges or O(n-1), where n is number of nodes
     """
    for i in range (len(root.kids)):
        zad(root.kids[i])
    if (root.kids == []):
        root.max_val = root.val
    else:
        sum = 0
        for el in root.kids:
            sum+=el.max_val
        root.max_val = max(root.val,sum)
    pass

a = Node(40)
b = Node(10)
c = Node(40)
f = Node(150)
g = Node(20)
d = Node(100)
k = Node(30)
e = Node(5)
a.kids.append(b)
a.kids.append(d)
a.kids.append(e)
b.kids.append(c)
b.kids.append(g)
c.kids.append(f)
d.kids.append(k)

zad(a)
print(max(a.max_val,a.val))