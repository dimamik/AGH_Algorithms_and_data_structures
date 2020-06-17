""" 
 Rozważmy drzewa BST, które dodatkowo w każdym węź-
le zawierają pole z liczbą węzłów w danym poddrzewie. Proszę opisać jak w takim drzewie wykonywać
następujące operacje:
1. znalezienie i-go co do wielkości elementu,
2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł
 """

class Node:
    def __init__(self,val=None,v=None):
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
        print(root.val)
        PrintBST(root.right)


def Insert(root, node_to_insert):
    if root == None:
        root = node_to_insert
    else:
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
    


r = Node(19,12) 
Insert(r,Node(10,7)) 
Insert(r,Node(21,4)) 
Insert(r,Node(3,3)) 
Insert(r,Node(12,3)) 
Insert(r,Node(21,4)) 
Insert(r,Node(20,1))
Insert(r,Node(36,2)) 
Insert(r,Node(74,1)) 
Insert(r,Node(1,1)) 
Insert(r,Node(7,1)) 
Insert(r,Node(11,1)) 
Insert(r,Node(18,1)) 

PrintBST(r)    
k=int (input())
print(Zad(r,k))
