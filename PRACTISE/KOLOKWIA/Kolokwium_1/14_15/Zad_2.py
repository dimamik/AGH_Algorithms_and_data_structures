class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next


class TwoLists_class():
    def __init__(self):
        self.even
        self.odd
def TwoLists(node_list):
    tmp=node_list
    parz=Node()
    nieparz=Node()
    ptr_p=parz
    ptr_n=nieparz
    while tmp!=None:
        if tmp.value%2==0:
            parz.next=tmp
            parz=parz.next
        else:
            nieparz=tmp
            nieparz=nieparz.next
        tmp=tmp.next
    if ptr_p.next!=None:ptr_p=ptr_p.next
    if ptr_n.next!=None:ptr_n=ptr_p.next
    to_ret=TwoLists_class()
    to_ret.even=ptr_p
    to_ret.odd=ptr_n
    return to_ret


