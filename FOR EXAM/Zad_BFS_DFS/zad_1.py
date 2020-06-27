class Node():
    def __init__(self,val=None):
        self.val=val
        self.next=None
class Queue():
    """ 
    Classic Queue on lists based on VALUE
     """
    def __init__(self):
        self.first=None
        self.last=self.first
        self.size=0
    def is_empty(self):
        return self.size==0
    def pop(self):
        """ 
        Gives the first element in the queue
         """
        if self.size==0:
            raise "size=0"
        self.size-=1
        if self.first.next!=None:
            to_ret=self.first.val
            self.first=self.first.next
            return to_ret
        else:
            tmp=self.first.val
            self.first=None
            self.last=None
            return tmp
    def put(self,val):
        """ 
        Puts value in the end of the queue
         """
        tmp=Node(val)
        self.size+=1
        if self.last==None:
            self.first=tmp
            self.last=self.first
            
        else:
            self.last.next=tmp
            self.last=tmp
""" 
TEST QUEUE
Q= Queue()
Q.put(45)
Q.put(15)
Q.put(10)
print(Q.pop())
print(Q.pop())
print(Q.pop())
print(Q.pop()) 
"""
class Vertex():
    """ 
    The way of using:
    [x,y,z], x-veris
     """
    def __init__(self):
        self.parrent=-1
        self.color=-1
        self.tab_index_incident=None
        self.visited=False
def BuildFromInc(tab):
    """ 
    Buduje z listy sąsiedstwa w postaci tablicy
    Lista sąsiedstwa tab
    tab=[[2,3],[1,5],...]
     """
    tab_of_v=[None]*len(tab)
    for i in range(len(tab)):
        V=Vertex()
        V.tab_index_incident=tab[i]
        tab_of_v[i]=V
    return tab_of_v

def Statek(M,T):
    """ Instead of value as an integer I have (i,j) """
    n=len(M)
    m=len(M[0])
    if M[n-1][m-1]<=T:
        return False
    tab_l_v=[None]*n
    for i in range(n):
        tab_l_v[i]=[None]*m
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j]<=T:
                M[i][j]=0
    """ Zaminiam nie dostateczne na zera """
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j]<=T:
                pass
            else:
                tmp=[]
                if i+1<n and M[i+1][j]!=0 :
                    tmp.append((i+1,j))
                if j+1<m and M[i][j+1]!=0:
                    tmp.append((i,j+1))
                if i-1>=0 and M[i-1][j]!=0:
                    tmp.append((i-1,j))
                if j-1>=0 and M[i][j-1]!=0:
                    tmp.append((i,j-1))
                V=Vertex()
                V.tab_index_incident=tmp
                tab_l_v[i][j]=V
    """ print(tab_l_v) """
    Q=Queue()
    si=0
    sj=0
    tab_l_v[si][sj].visited=True
    tab_l_v[si][sj].parrent=None
    Q.put((si,sj))
    while Q.size!=0:
        s=Q.pop()
        for v in tab_l_v[s[0]][s[1]].tab_index_incident:
            if not tab_l_v[v[0]][v[1]].visited:
                tab_l_v[v[0]][v[1]].visited=True
                tab_l_v[v[0]][v[1]].parrent=s
                Q.put(v)
    #print(tab_l_v[n-1][m-1].visited==True)
    if tab_l_v[n-1][m-1].visited==True:
        tmp_p=tab_l_v[n-1][m-1].parrent
        M[n-1][m-1]='X'
        M[0][0]='X'
        while tmp_p!=None and tmp_p!=-1:
            M[tmp_p[0]][tmp_p[1]]='X'
            tmp_p=tab_l_v[tmp_p[0]][tmp_p[1]].parrent
        for i in range(n):
            for j in range(m):
                print(M[i][j], end=" ")
            print()
    return tab_l_v[n-1][m-1].visited==True




tab = [
    [5,5,5,5,5],
    [5,4,4,5,5],
    [5,4,4,5,5],
    [5,5,5,4,5]
 ]         
print(Statek(tab,4)  )






    
    
