class Node():
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class stack_lists():
    def __init__(self,size=0):
        first=Node()
        self.first=first
        self.size=size
    def pop(self):
        if self.size==0:return
        self.size-=1
        tmp=self.first.next.next
        to_ret=self.first.next
        self.first.next=tmp
        return to_ret
    def push(self,Node_to_push):
        tmp=self.first.next
        Node_to_push.next=tmp
        self.first.next=Node_to_push
        self.size+=1
    def print_stack(self):
        if self.size==0:print("The stack is empty")
        tmp=self.first.next
        while tmp!=None:
            print(tmp.val)
            tmp=tmp.next
        
""" 
S=stack_lists()
K=Node(5)
S.push(K)
S.print_stack()
S.pop()
S.print_stack()

 """

class stack():
    def __init__(self,size=10):
        tab=[None]*size
        self.tab=tab
        self.top=0 #Current to fill
        self.size=size
    def pop(self):
        self.top-=1
        return self.tab[self.top]
    def push(self,element_to_push):
        self.tab[self.top]=element_to_push
        self.top+=1
    def is_empty(self):
        return self.size==0
    def print_stack(self):
        print(self.tab[:self.top])

class Queue():
    def __init__(self,size_of_tab=10):
        self.size_of_tab=size_of_tab
        tab=[None]*size_of_tab
        self.tab=tab
        self.first=0
        self.size=0
    def pop(self):
        self.size-=1
        self.first+=1
        return self.tab[self.first-1]
    def push(self,el_to_push):
        self.size+=1
        tmp=self.first+self.size-1
        self.tab[tmp]=el_to_push
    def print_queue(self):
        tab_tmp=[0]*self.size
        k=0
        for i in range(self.first,self.first+self.size):
            tab_tmp[k]=self.tab[i]
            k+=1
        print(tab_tmp)
""" 

K=Queue()
K.push(6)
K.push(6)
K.push(6)
K.push(6)
K.pop()
K.print_queue()

 """


    



        