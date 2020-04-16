class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class LinkedLists():
    def __init__(self):
        self.first=None
        self.last=None
    def make_from_array(self,tab):
        if len(tab)==0:return
        self.first=Node(tab[0])
        p = self.first
        self.last=p
        for i in range(1,len(tab)):
            q=Node(tab[i])
            p.next=q
            p=q
            self.last=p

X=LinkedLists()
X.make_from_array([1,2,3])
print(X.first.value)