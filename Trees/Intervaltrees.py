#TODO
""" 
1. Przechowanie wezlow w tablice

 """
class NodeInTab():
    def __init__(self):
        self.przedzial
        self.val
        self.leaf=False
    def __eq__(self, value):
        return super().__eq__(value)
    pass
tab=[]
def sortedArrayToBST(arr):
    if not arr: 
        return None
    # find middle 
    mid = (len(arr)) // 2
    # make the middle element the root 
    tab.append(arr[mid]) 
    # left subtree of root has all 
    # values <arr[mid] 
    tab.append( sortedArrayToBST(arr[:mid]) )
    # right subtree of root has all  
    # values >arr[mid] 
    tab.append(sortedArrayToBST(arr[mid+1:])) 
    
def sortedArrayToBSTArray(arr,tab_to_ret,l,r):
    while l<r:
        mid = (l+r) // 2
        tab_to_ret.append(arr[mid])
        sortedArrayToBSTArray(arr,tab_to_ret,l,mid)
        sortedArrayToBSTArray(arr,tab_to_ret,mid,r)
    

print(sortedArrayToBST([0,5,7,10,12,15,20]))
print(tab)




    


    


