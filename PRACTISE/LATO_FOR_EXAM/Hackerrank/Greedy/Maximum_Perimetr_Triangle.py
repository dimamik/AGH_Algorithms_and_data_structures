# Complete the maximumPerimeterTriangle function below.
def IsTriangle(a,b,c):
    if (a>=b+c):
        return False
    if (c>=a+b):
        return False
    if (b>=a+c):
        return False
    return True


def maximumPerimeterTriangle(tab):
    tab = sorted(tab)
    for a,b,c in zip(range(len(tab)-1,1,-1),range(len(tab)-2,0,-1),range(len(tab)-3,-1,-1)):
        if (IsTriangle(tab[a],tab[b],tab[c])):
            return tab[c],tab[b],tab[a]
    return (-1)
print(maximumPerimeterTriangle([1 ,2 ,3]))
