class Node:
    def __init__(self = None, value = None):
        self.value=value
        self.next = None


    def _out(self):
        """ Outputs list, takes first element """
        new_list=self
        tab = []
        while new_list!= None:
            tab.append(new_list.value)
            new_list=new_list.next
        print(tab)
    def _in(self,n):
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
    def _add_to_end(self,val):
        first=self
        while first.next!= None:
                first=first.next
        el_to_add=Node()
        el_to_add.value = val
        first.next=el_to_add
    def _del_all(self):
        return None
    def _add_to_beg(self,val):
        tmp=Node(val)
        tmp.value=val
        if self.value!=None:
            tmp.next=self
            print("S")
            return tmp
        else:
            tmp.next=None
            return tmp
    def _add_to_end_list(self,lista_to_add):
        if self == None:
            return lista_to_add
        else :
            last_lista=self
            last_lista.next=lista_to_add
            return lista_to_add


def usun_el(prev,el_do_us):
    #Pracujemy z wartownikiem
    prev.next=el_do_us.next
    print("Funkcja usun przel na",prev.next)


def Selection_sort(first):
    wartownik = Node(-1)
    wartownik.next= first
    #Ogolnie algorytm bedzie polegal na wyznaczeniu min i usunieciu go w inna
    #tablice
    tab_to_return=Node() 
    tab_ret = tab_to_return
    lenght=first._len()
    print(lenght)
    for _ in range(lenght):
        tmp_i_prev=wartownik
        tmp_i=tmp_i_prev.next
        min_el=tmp_i
        #print("Current min is",min_el.value)
        min_el_prev=tmp_i_prev
        while tmp_i!=None:
            print("Sprawdzam",tmp_i.value)
            if min_el.value>tmp_i.value:
                min_el=tmp_i
                print("Min_Element",min_el.value)
                min_el_prev=tmp_i_prev
                print("Min_El next",min_el.next)
            tmp_i_prev=tmp_i
            tmp_i=tmp_i.next

        tab_to_return = tab_to_return._add_to_end_list(min_el)
        print("Usuwam",min_el.value)
        usun_el(min_el_prev,min_el)
    return tab_ret.next

def switch(prev,l1,l2):
    prev.next=l2
    l1.next=l2.next
    l2.next=l1
    return l2  
def Bubble_sort(first):
    length=first._len()
    wartownik = Node()
    wartownik.value=0
    wartownik.next=first
    tmp=first
    for _ in range(length-1):
        tmp = wartownik.next
        prev=wartownik
        while tmp.next != None:
            #print(tmp.next)
            if tmp.value>tmp.next.value:
                switch(prev,tmp,tmp.next)
                prev=prev.next
            else:
                prev=prev.next
                tmp=tmp.next      
    #Usuwanie wartownika
    wartownik=wartownik.next
    return wartownik
