""" 
Left Node<=root<Right Node
Without parrent
 """
class Node:
    """ 
    Should predefine value
     """
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.parent=None


def PrintBST(root):
    """ 
    Function to print BST tree as a sorted array
     """
    if root:
        PrintBST(root.left)
        print(root.val)
        PrintBST(root.right)
def PrintParent(root):
    if root:
        PrintBST(root.left)
        print(root.val, root.parent)
        PrintBST(root.right)

def Insert(root, node_to_insert,parent=None):
    
    if root == None:
        root = node_to_insert
    else:
        if node_to_insert.val > root.val:
            if root.right == None:
                root.right = node_to_insert
                node_to_insert.parent=root.val
            else:
                Insert(root.right, node_to_insert,root)
                
        else:
            if root.left == None:
                root.left = node_to_insert
            else:
                Insert(root.left, node_to_insert,root)
    

def Search(root, val_to_search):
    if root == None or root.val == val_to_search:
        return root
    if root.val > val_to_search:
        return Search(root.left, val_to_search)
    elif root.val < val_to_search:
        return Search(root.right, val_to_search)

ilosc=0
suma=0
def zad(root):
    global suma
    global ilosc
    if root!=None:
        zad(root.left)
        suma+=root.val
        ilosc+=1
        zad(root.right)

r = Node(50) 
Insert(r,Node(30)) 
PrintParent(r)
Insert(r,Node(20)) 
Insert(r,Node(40)) 
Insert(r,Node(70)) 
zad(r)
print(suma/ilosc)