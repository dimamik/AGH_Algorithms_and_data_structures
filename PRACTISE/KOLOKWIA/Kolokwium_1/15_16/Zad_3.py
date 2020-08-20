class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
def add_to_its_sorted_place(Node,node_to_add):
        tmp=Node
        if tmp==None:
            node_to_add.next=None
            return
        if node_to_add.value<=Node.value:
            node_to_add.next=Node
            Node=node_to_add
        prev=None
        while tmp!=None and tmp.value<node_to_add.value  : 
            prev=tmp
            tmp=tmp.next
        prev.next=node_to_add
        node_to_add.next=tmp
def fixSortedList(L):
    tmp=L
    while tmp.next!=None and tmp.value<tmp.next.value:
        tmp=tmp.next
    add_to_its_sorted_place(L,tmp)

    
    print(tmp.value)

X=Node(1)
Y=Node(2)
Z=Node(1)

fixSortedList(X)
