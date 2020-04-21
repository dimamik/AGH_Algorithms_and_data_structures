class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class LinkedList():
    def __init__(self,first=None,last=None):
        self.first=first
        self.last=last
    def MakeFromNode(self,node):
        """ 
        Robi z Node LinkedList in O(n)
         """
        self.first=node
        tmp=self.first
        while tmp!=None:
            tmp=tmp.next
        self.last=tmp
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
    def isEmpty(self):
        return self.first is None
    def hasOneElement(self):
        if self.first==None:return False
        return self.first == self.last
    def print_list_as_tab(self):
        if self.first==None:
            return
        tmp=self.first
        tab_to_ret=[]
        while tmp!=self.last:
            tab_to_ret.append(tmp.value)
            tmp=tmp.next
        if tmp.value!=None:
            tab_to_ret.append(tmp.value)
        return tab_to_ret
    def print_to_console(self):
        tmp=self.first
        while tmp!=None:
            print(tmp.value)
            tmp=tmp.next
    def add_to_end(self,node_to_add):
        if self.first==self.last==None:
            self.first=node_to_add
            self.last=node_to_add
            node_to_add.next=None
            return
        tmp=self.last
        tmp.next=node_to_add
        self.last=node_to_add
        """ To avoid consequenses of chain adding """
        #node_to_add.next=None
    def add_to_beg(self,node_to_add):
        tmp=self.first
        if tmp==None:
            self.last=node_to_add
        node_to_add.next=tmp
        self.first=node_to_add
    def add_value(self, val):
        node = Node(val)
        if self.isEmpty():
            self.first = node
            self.last = node
            return
        self.last.next = node
        self.last = node
    def size_of(self):
        tmp=self.first
        count=0
        while tmp!=None:
            count+=1
            tmp=tmp.next
        return count

        
    def add_to_index_i_from_0(self,node_to_add,index):
        """ 
        Adding to index i or if there is no such, to the end
         """
        tmp=self.first
        if tmp==None:
            self.first=node_to_add
            self.last=node_to_add
            node_to_add.next=None
            return
        for i in range(index-1):
            if tmp.next!=None:
                tmp=tmp.next
        tmp_next=tmp.next
        tmp.next=node_to_add
        node_to_add.next=tmp_next
        if tmp_next==None:
            self.last=node_to_add
    def add_to_its_sorted_place(self,node_to_add):
        tmp=self.first
        if tmp==None:
            self.first=node_to_add
            self.last=node_to_add
            node_to_add.next=None
            return
        if node_to_add.value<=self.first.value:
            node_to_add.next=self.first
            self.first=node_to_add
            return
        Tr=True
        prev=None
        while tmp!=None and tmp.value<node_to_add.value  : 
            prev=tmp
            tmp=tmp.next
        prev.next=node_to_add
        node_to_add.next=tmp
        if tmp==None:
            self.last=node_to_add
    def del_from_end(self):
        #Need to find the previous element
        tmp=self.first
        if tmp==None:return
        if tmp.next==None:
            self.first=None
            self.last=None
            return
        while tmp.next.next!=None:
            tmp=tmp.next
            print(tmp.value)
        to_del=self.last
        self.last=tmp
        del to_del
    def del_from_begining(self):
        tmp=self.first
        if tmp==None or tmp.next==None:
            self.first=None
            self.last=None
            return
        self.first=tmp.next
        del tmp
    def is_present(self,el_val):
        tmp=self.first
        while tmp!=None:
            if tmp.value==el_val:
                return True
            tmp=tmp.next
        return False
    def Find_Node_By_Value(self,el_val):
        tmp=self.first
        while tmp!=None:
            if tmp.value==el_val:
                return tmp
            tmp=tmp.next
        return None
    def switch(self,prev,curr):
        """ 
        Dziala tylko z wartownikiem!
         """
        nast_el=curr.next
        if nast_el.next==None:
            self.last=curr
        tmp=nast_el.next
        nast_el.next=curr
        curr.next=tmp
        prev.next=nast_el
    def Bubble_sort(self):
        wartownik=Node(0)
        wartownik.next=self.first
        for _ in range(self.size_of()):
            curr=wartownik.next
            prev=wartownik
            while curr.next!=None:
                #print("Checking",curr.value,"and",curr.next.value)
                if curr.value>curr.next.value:
                    self.switch(prev,curr)
                    prev=prev.next
                else:
                    prev=curr
                    curr=curr.next
        self.first=wartownik.next

    def Insertion_Sort(self):
        Sorted=LinkedList()
        tmp=self.first
        while tmp!=None:
            to_add=tmp
            tmp=tmp.next
            Sorted.add_to_its_sorted_place(to_add)
        self.first=Sorted.first
        self.last=Sorted.last
    def SplitLinkedList(self):
        len = self.size_of()
        newBegin = self.first
        newEnd = self.first
        for _ in range(0, len//2):
            newEnd = newBegin
            newBegin = newBegin.next
        newBegin = newEnd.next
        newEnd.next = None
        return (LinkedList(self.first, newEnd), LinkedList(newBegin,self.last))
    def Merge_Sort(self): 
        """ 
        Returns LinkedList and not working instantly
        X=X.Merge_Sort()
         """
        if self.isEmpty() or self.hasOneElement():
            return self
        firstHalf, secondHalf =self.SplitLinkedList()
        firstHalfSorted = firstHalf.Merge_Sort()
        secondHalfSorted = secondHalf.Merge_Sort()
        return Merge_On_Lists(firstHalfSorted, secondHalfSorted)
    def Radix_Sort(self):
        pass
    def FindMaxEl(self):
        if self.first==None:
            return None
        tmp=self.first
        max_el=tmp.value
        while tmp!=None:
            max_el=max(max_el,tmp.value)
            tmp=tmp.next
        return max_el
    def Bucket_Sort(self,n=False):
        """ 
        Dziala tylko dla jednostajnego rozkladu danych w listach
        """
        #Rozdialnosc Bucketa -> parametr dla najlepszego rozkladu
        #Im lepiej rozklad, tym mniej zlozonosc
        """ 
        Rozd Bucketa ->       max_el/ilosc_elementow
        Ilosc Bucketow ->     Max_el/rozd_Bucketa=ilosc_elementow
        ind Bucketa dla el -> El/rozd_Bucketa
        """
        max_el=self.FindMaxEl()
        ilosc_elem=self.size_of()
        if ilosc_elem==0:
            return None
        Rozdz_Bucketa=max_el/ilosc_elem
        tab_of_Buckets=[None]*(ilosc_elem+1)
        for i in range(ilosc_elem+1):
            tab_of_Buckets[i]=LinkedList()
        tmp=self.first
        while tmp!=None:
            copy_to_add=Node(tmp.value)
            index=int (tmp.value/Rozdz_Bucketa)
            tab_of_Buckets[index].add_to_its_sorted_place(copy_to_add)
            tmp=tmp.next
        to_ret=LinkedList()
        for i in range(ilosc_elem+1):
            pt=tab_of_Buckets[i].first
            if pt==None:
                continue
            to_ret.add_to_end(pt)
        return to_ret
            

X=LinkedList()
arr=[1]
X.make_from_array(arr)
tab = X.Bucket_Sort()
print(tab.print_list_as_tab())





def Merge_On_Lists(List1, List2):
    if List1.isEmpty():
        return List2
    result = LinkedList()
    p = Node()
    q = Node()
    r = Node()
    if List1.first.value <= List2.first.value:
        result.first = List1.first
        r = result.first
        result.last = r
        p = List1.first.next
        q = List2.first
    else:
        result.first = List2.first
        r = result.first
        result.last = r
        p = List2.first.next
        q = List1.first
    while p is not None and q is not None:
        while p is not None and q is not None and p.value <= q.value:
            r.next = p
            r = r.next
            result.last = r
            p = p.next
        while q is not None and p is not None and q.value <= p.value:
            r.next = q
            r = r.next
            result.last = r
            q = q.next
    while p is not None:
        r.next = p
        r = r.next
        result.last = r
        p = p.next
    while q is not None:
        r.next = q
        r = r.next
        result.last = r
        q = q.next
    return result
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














