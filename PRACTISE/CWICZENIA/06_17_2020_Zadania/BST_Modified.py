""" 
 Rozważmy drzewa BST, które dodatkowo w każdym węź-
le zawierają pole z liczbą węzłów w danym poddrzewie. Proszę opisać jak w takim drzewie wykonywać
następujące operacje:
1. znalezienie i-go co do wielkości elementu,
2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł
Wersja bez modyfikacji
 """

class Node:
    def __init__(self,val=None,v=1):
        self.left=None
        self.right=None
        self.val=val
        self.v=v

def PrintBST(root):
    """ 
    Function to print BST tree as a sorted array
     """
    if root:
        PrintBST(root.left)
        print("Val=",root.val,"losc elementów w poddrzewie: ",root.v)
        PrintBST(root.right)
def Insert(root, node_to_insert):
    if root == None:
        root = node_to_insert
    else:
        #Added incrementation of v
        root.v+=1
        if node_to_insert.val > root.val:
            
            if root.right == None:
                root.right = node_to_insert
            else:
                Insert(root.right, node_to_insert)
        else:
            
            if root.left == None:
                root.left = node_to_insert
            else:
                Insert(root.left, node_to_insert)


def Search(root, val_to_search):
    if root == None or root.val == val_to_search:
        return root
    if root.val > val_to_search:
        return Search(root.left, val_to_search)
    elif root.val < val_to_search:
        return Search(root.right, val_to_search)


def MinValNode(node):
    tmp = node
    while (tmp.left != None):
        tmp = tmp.left
    return tmp


def Delete(root, val_to_del):
    if root == None:
        return root
    if root.val > val_to_del:
        root.left = Delete(root.left, val_to_del)
    elif root.val < val_to_del:
        root.right = Delete(root.right, val_to_del)
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
        tmp = MinValNode(root.right)
        root.val = tmp.val
        root.right = Delete(root.right, tmp.val)
    return root


def Zad(root,i):
    """ 
    Function to find i-th max element in BST tree
     """
    if i>root.v:
        return None
    v_p=0
    if root !=None and root.right!=None:
        v_p=root.right.v
    if i==v_p+1:
        return root.val
    if i>v_p : return Zad(root.left,i-1-v_p)
    else:
        return Zad(root.right,i)
    



def FindParent(root,node_to_find_parent):
    if root == None or root.left == node_to_find_parent or root.right==node_to_find_parent:
        return root
    if root.val > node_to_find_parent.val:
        return FindParent(root.left, node_to_find_parent)
    elif root.val < node_to_find_parent.val:
        return FindParent(root.right, node_to_find_parent)
    pass

def KtoryCoDoWielkosci(node, parent,root):
    """ 
    Ewentualnie potrzebuje pola parent, żeby zobaczyć, jakim dzieckiem jestem
     """
    i=0
    if node.right!=None:
        i+=node.right.v
    if parent!=None:
        if parent.val>node.val:
            i+=root.v
            if node.left!=None:
                i-=node.left.v
    return i


r= Node(5)
p_s=Node(3)
Insert(r,p_s)
s=Node(2)
Insert(r,s)
Insert(r,Node(15))
print("Ktory co do wielkosci:")
print(KtoryCoDoWielkosci(s,FindParent(r,s),r))
""" print(FindParent(r,s).val) """
""" r = Node(19,12) 
Insert(r,Node(10,7)) 
Insert(r,Node(21,4)) 


k=int (input())
print(Zad(r,k))
"""

PrintBST(r)    

