class Node:
    def __init__(self = None,value = None):
        self.value=value
        self.next = None
        if value!=None:
            self.is_empty=True
        else:
            self.is_empty=False
        #self.state = None
    def _out(self):
        new_list=self
        tab = []
        while new_list!= None:
            tab.append(new_list.value)
            new_list=new_list.next
        print(tab)
    def _in(self,n=2):
        new_obj=Node()
        to_return = new_obj
        for _ in range(n-1):
            tmp=Node()
            new_obj.value=int (input())
            new_obj.next = tmp
            new_obj = tmp
        new_obj.value = int (input())
        new_obj.next=None
        return to_return
    def _len(self):
        tmp=self
        counter=0
        while tmp!= None:
            counter+=1
            tmp=tmp.next
        return int (counter)
    def _add_value_to_end(self,val):
        first=self
        while first.next!= None:
                first=first.next
        el_to_add=Node()
        el_to_add.value = val
        first.next=el_to_add
    def _add_value_to_beg(self,val):
        tmp=Node(val)
        tmp.value=val
        if self.value!=None:
            tmp.next=self
            print("S")
            return tmp
        else:
            tmp.next=None
            return tmp
    def _add_list_to_end_return_last(self,lista_to_add):
        """ 
        Taking the the end of a current list and connecting it with lista_to_add, or
        if self==None returning lista_to_add (Last value)
         """
        if self.value == None:
            return lista_to_add
        else :
            last_lista=self
            last_lista.next=lista_to_add
            return lista_to_add
    def _add_list_to_end_return_first(self,lista_to_add):
        """ 
        Getting first el of the list and connects it to the other list
         """
        if self.value == None:
            return lista_to_add
        tmp=self
        while tmp.value!=None:
            tmp=tmp.next
        tmp.next=lista_to_add
        return self

X=Node()
X=X._in()
X._out()
Y=Node()
Y=Y._in()
Y=Y._add_list_to_end(X)
Y._out()
