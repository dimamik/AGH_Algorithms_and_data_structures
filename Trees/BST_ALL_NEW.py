class Node():
    """ 
    Dziala po wartosci key,
    Z lewej strony <
    Z prawej >
     """
    def __init__(self,key=None):
        self.val=None
        self.key=key
        self.parent=None
        self.right=None
        self.left=None
        
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

def BSTMakeFromSortedArray(tab):
    """ _I
    With using PYTHON TRICKS 
    WITHOUT PARENTS
    """
    if len(tab)<=0:
        return None
    mid = len(tab)//2
    root=Node(tab[mid])
    root.left=BSTMakeFromSortedArray(tab[:mid])
    root.right=BSTMakeFromSortedArray(tab[mid+1:])
    return root

""" r=BSTMakeFromSortedArray([1,2,3,4,5])
PrintTheTree(r) """

def MinBST(root):
    if root==None:
        return None
    while root.left!=None:
        root=root.left
    return root
def MaxBST(root):
    if root==None:
        return None
    while root.right!=None:
        root=root.right
    return root
def Insert(root,key_to_find_succ):
    """ 
    Takes node and inserts it in the right place
    With parent tab modification
     """
    if root==None:
        return key_to_find_succ
    if root.key>key_to_find_succ.key:
        tmp=Insert(root.left,key_to_find_succ)
        root.left=tmp
        tmp.parent=root
    else:
        tmp=Insert(root.right,key_to_find_succ)
        root.right=tmp
        tmp.parent=root
    return root


def SuccBST(root,key_val):
    """ Nastepnik w posortowanej tablice """
    if root==None:
        return
    if root.key==key_val:
        """ Minimalna wartosc w prawym poddrzewie -> succ"""
        k=root
        k_tmp=MinBST(root.right)
        if k_tmp!=None:
            return k_tmp
        else:
            while k!= None and k.parent!=None and k.parent.key<k.key:
                k=k.parent
            if k!=None and k.parent!=None:
                return k.parent
            else:
                return k
    if root.key<key_val:
        return SuccBST(root.right,key_val)
    else:
        return SuccBST(root.left,key_val)

""" r=BSTMakeFromSortedArray([1,7,15,28,190,256])
PrintTheTree(r)
print(SuccBST(r,28).key) """

def PreccBST(root,key_val):
    """ Poprzednik w posortowanej tablice """
    if root==None:
        return
    if root.key==key_val:
        k=root
        k_tmp=MaxBST(root.left)
        if k_tmp!=None:
            return k_tmp
        else:
            while k!= None and k.parent!=None and k.parent.key>k.key:
                k=k.parent
            if k!=None and k.parent!=None:
                return k.parent
            else:
                return k
    if root.key<key_val:
        return PreccBST(root.right,key_val)
    else:
        return PreccBST(root.left,key_val)

def DeleteBST(root,key_to_del):
    """ hard implementation if we are taking care of parents """
    
    pass

def DeleteBSTWithoutParents(root, val_to_del):
    if root == None:
        return root
    if root.key > val_to_del:
        root.left = DeleteBSTWithoutParents(root.left, val_to_del)
    elif root.key < val_to_del:
        root.right = DeleteBSTWithoutParents(root.right, val_to_del)
    #Found a Node to delete
    else:
        if root.left == None:
            tmp = root.right
            root = None
            return tmp
        elif root.right == None:
            tmp = root.left
            root = None
            return tmp
        #If we have Node with 2 kids than we need to dinf succ
        tmp = MinBST(root.right)
        root.key = tmp.key
        root.right = DeleteBSTWithoutParents(root.right, tmp.key)
    return root


""" r=BSTMakeFromSortedArray([1,7,15,28,190,256])
DeleteBSTWithoutParents(r, 28)
PrintTheTree(r) """

def DeleteBSTWithParents(root, key):
    """ 
    !Uwaga I!
     """
    curr = root
    while curr and curr.key != key:
        parent = curr
        if key < curr.key:
            curr = curr.left
        else:
            curr = curr.right

    if curr is None:
        return root

    if curr.left is None and curr.right is None:
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        else:
            root = None

    elif curr.left and curr.right:
        min_key = MinBST(curr.right)
        val = min_key.key

        DeleteBSTWithParents(root, min_key.key)
        curr.key = val
    else:
        """ Jedno Dziecko """
        if curr.left:
            child = curr.left
        else:
            child = curr.right
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:
            root = child
    return root


""" r=Node(15)
Insert(r,Node(10))
Insert(r,Node(16))
Insert(r,Node(19))
Insert(r,Node(18))
Insert(r,Node(17))
Insert(r,Node(1))
Insert(r,Node(215))
Insert(r,Node(278))
Insert(r,Node(13))
Insert(r,Node(4))
Insert(r,Node(14))
PrintTheTree(r)
DeleteBSTWithParents(r, 19)
print(SuccBST(r,215).key) """
