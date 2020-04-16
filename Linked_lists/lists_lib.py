class Node():
    def __init__(self,value=None,next=None):
        self.value=value
        self.next=next
class LinkedList():
    def __init__(self,first=None,last=None):
        self.first=first
        self.last=last
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
    def add_to_beg(self,node_to_add):
        tmp=self.first
        if tmp==None:
            self.last=node_to_add
        node_to_add.next=tmp
        self.first=node_to_add
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
        if node_to_add.value<self.first.value:
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
        


    def switch(self,prev,f):
        s=f.next
        if s==None:return
        #First one
        if prev==None and f==self.first:
            self.first=s
        if s.next==None:
            self.last=f
        f.next=s.next
        s.next=f


X=LinkedList()
arr=[0,1,2]
X.make_from_array(arr)
K=Node(3)
X.add_to_its_sorted_place(K)
tab=X.print_list_as_tab()
X.print_to_console()
print(tab)

        









