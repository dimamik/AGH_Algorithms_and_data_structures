class Node():
    """ 
    Dziala po wartosci key,
    Z lewej strony <
    Z prawej >
     """
    def __init__(self,key=None,index=None):
        """ 
        index jest rowny ilosci node'ow w poddrzewie
         """
        self.val=None
        self.key=key
        self.parent=None
        self.right=None
        self.left=None
        self.index=index
  
def PrintTheTree(root):
    if root!=None:
        PrintTheTree(root.left)
        print(root.key, end=" ")
        if root.parent!=None:
            print(root.parent.key)
        else:
            print("NONE")
        PrintTheTree(root.right)

def FindBST(root,key_to_find):
    """ 
    Returns Node with the key_to_find 
    or None if nothing found
     """
    while root!=None:
        if root.key==key_to_find:
            return root
        elif root.key>key_to_find:
            root=root.left
        else:
            root=root.right
    return None

def FindiMinEl(root,i):
    while i<=root.index+1:
        """ if root.left.index+1==i:
            return root """
        if (root.left==None and root.index==i) or (root.left!=None and root.left.index+1==i):
            return root
        elif root.left.index+1<i:
            return FindiMinEl(root.right,i-root.left.index-1)
        elif root.left.index+1>i:
            return FindiMinEl(root.left,i)
    return None
ilosc=0
def zadb(root,key):
    global ilosc
    """ 
    Wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł
     """
    if FindBST(root,key)==None:
        return None
    while root!=None:
        if root.key==key:
            l=1
            if root.left!=None:
                l+=root.left.index
            return ilosc+l
        elif root.key<key:
            ilosc+=(1+root.left.index)
            return zadb(root.right,key)
        elif root.key>key:
            return zadb(root.left,key)
    return ilosc


    

r = Node(15,8)
x=Node(10,3)
r.left=x
y=Node(3,1)
x.left=y
z=Node(14,1)
x.right=z
k=Node(20,4)
r.right=k
p=Node(17,2)
k.left=p
m=Node(16,1)
p.left=m
o=Node(30,1)
k.right=o
PrintTheTree(r)

print(FindiMinEl(r,8).key)
print(zadb(r,17))