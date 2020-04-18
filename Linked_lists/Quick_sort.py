from lists_lib import *
def ConcatenateLinkedLists(arrayOfLinkedLists):
    """ 
    Bit Algo Function
     """
    result = LinkedList()
    foundBegining = False
    for i in arrayOfLinkedLists:
        if not i.isEmpty():
            i.last.next  = None
    for i in arrayOfLinkedLists:
        if not foundBegining and not i.isEmpty():
            foundBegining = True
            result.first = i.first
            result.last = i.last
        elif not i.isEmpty():
            result.last.next = i.first
            result.last = i.last
    return result

def QuickSortOnLinkedList(List):
    """ 
    Bit Algo Function
     """
    if List.isEmpty() or List.hasOneElement():
        return List
    smaller = LinkedList()
    equal = LinkedList()
    greater = LinkedList()
    p = List.first
    while p is not None:
        if p.value<List.last.value:
            smaller.add_value(p.value)
        elif p.value == List.last.value:
            equal.add_value(p.value)
        else:
            greater.add_value(p.value)
        p=p.next
    return ConcatenateLinkedLists([QuickSortOnLinkedList(smaller), equal, QuickSortOnLinkedList(greater)])


X=LinkedList()
arr=[4,3,2]
X.make_from_array(arr)
X=QuickSortOnLinkedList(X)
print(X.print_list_as_tab())