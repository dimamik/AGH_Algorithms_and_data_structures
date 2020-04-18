class Node():
    def __init__(self,value=None,next=None):
        self.value = None
        self.next = None
        self.prev = None

def init_the_node(k):
    first = Node()
    to_ret=first
    for _ in range(k-1):
        tmp=Node()
        value=int (input())
        first.value=value
        first.next=tmp
        first=tmp
    first.value=input()
    first.next=None
    return to_ret
def list_out(first):
    while first!=None:
        print(first.value)
        first=first.next

def add_node_to_end(first,node_to_add):
    if first.value!=None:
        while first.next!=None:
            first=first.next
        first.next=node_to_add
        return node_to_add
    else:
        first.value=node_to_add.value
        return node_to_add
def insertion_sort(first):
    if first.value==None:return None
    first_of_sorted=first
    curr_adding=None
    curr_slicing = first.next
    while curr_slicing.value!=None:
        tmp=first_of_sorted
        #inputting the current_slicing into curr_adding
        while curr_slicing.value>=tmp.value and  curr_slicing=curr_slicing.next




    






        


