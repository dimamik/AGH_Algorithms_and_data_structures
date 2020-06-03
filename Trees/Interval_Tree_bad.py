class IntervalTreeNode():
    def __init__(self,val):
        self.parrent=None
        self.left=None
        self.right=None
        self.intervals=None
        self.val=val

def PrintBST(root):
    """ 
    Function to print BST tree as a sorted array
     """
    if root:
        PrintBST(root.left)
        print(root.val)
        PrintBST(root.right)

def Insert(root, IntervalTreeNode_to_insert):
    if root == None:
        root = IntervalTreeNode_to_insert
    else:
        if IntervalTreeNode_to_insert.val > root.val:
            if root.right == None:
                root.right = IntervalTreeNode_to_insert
            else:
                Insert(root.right, IntervalTreeNode_to_insert)
        else:
            if root.left == None:
                root.left = IntervalTreeNode_to_insert
            else:
                Insert(root.left, IntervalTreeNode_to_insert)


def Search(root, val_to_search):
    if root == None or root.val == val_to_search:
        return root
    if root.val > val_to_search:
        return Search(root.left, val_to_search)
    elif root.val < val_to_search:
        return Search(root.right, val_to_search)


def MinValIntervalTreeNode(IntervalTreeNode):
    tmp = IntervalTreeNode
    while (tmp.left != None):
        tmp = tmp.left
    return tmp

""" 
Преобразовать посортированный массив в сбалансированное бст дерево

 """
def Delete(root, val_to_del):
    if root == None:
        return root
    if root.val > val_to_del:
        root.left = Delete(root.left, val_to_del)
    elif root.val < val_to_del:
        root.right = Delete(root.right, val_to_del)
    #Found a IntervalTreeNode to delete
    else:
        if root.left == None:
            tmp = root.right
            root = None
            return tmp
        elif root.right == None:
            tmp = root.left
            root = None
            return tmp
        #If we have IntervalTreeNode with 2 kids than we need to dinf succ
        tmp = MinValIntervalTreeNode(root.right)
        root.val = tmp.val
        root.right = Delete(root.right, tmp.val)
    return root
def sortedArrayToBST(arr):
    if not arr: 
        return None
    # find middle 
    mid = (len(arr)) // 2
    root = IntervalTreeNode(arr[mid])  
    root.left = sortedArrayToBST(arr[:mid]) 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 
def AddLeafsToTree(BSTRoot,BSTprev,is_left):
    tmp=BSTRoot
    while tmp!=None:
        AddLeafsToTree(tmp.left,tmp,1)
        AddLeafsToTree(tmp.right,tmp,0)
    left_leaf=IntervalTreeNode(-1)
    right_leaf=IntervalTreeNode(-1)
    tmpprev=BSTprev
    if is_left:
        tmpprev.left=left_leaf
    if not is_left:
        tmpprev.right=right_leaf






    
def FromPrzedzalsToTree(tab):
    tab_of_numbers=[]
    for i in range(len(tab)):
        tab_of_numbers.append(tab[i][0])
        tab_of_numbers.append(tab[i][1])
    tab_of_numbers=sorted(set(tab_of_numbers))
    BSTRoot=sortedArrayToBST(tab_of_numbers)
    #AddLeafsToTree(BSTRoot,None,-1)
    PrintBST(BSTRoot)
    

tab=[[0,10],[5,20],[7,12],[10,15]]
FromPrzedzalsToTree(tab)