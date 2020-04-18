""" 
1. Dana jestr struktura opisująca listę jednokierunkową dla liczb rzeczywistych:
struct Node{ Node* next; double value; }
Proszę zaimplementować funkcję void Sort( Node* list ), która otrzymuje na wejściu listę
liczb rzeczywistych (z wartownikiem), wygenerowaną zgodnie z rozkładem jednostajnym na
przedziale [0,10) i sortuje jej zawartość w kolejności niemalejącej. Funkcja powinna być możliwie
jak najszybsza (biorąc pod uwagę warunki zadania). Proszę oszacować złożoność
zaimplementowanej funkcji.
 """

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
arr=[10,2,4,7,8]
X.make_from_array(arr)
tab = X.Bucket_Sort()
print(tab.print_list_as_tab())


""" 
Złożoność funkcji: O(n)

 """