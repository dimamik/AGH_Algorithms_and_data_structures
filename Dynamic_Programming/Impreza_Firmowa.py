
class TreeForTask():
    def __init__(self,fun):
        self.root = Employee(fun)
    def build(self,tab):
        # self.root.emp.append(list(map(Employee,tab)))
        for i in range(len(tab)):
            self.root.emp.append(Employee(tab[i]))
class Employee():
    def __init__(self,fun):
        """ 
        Drzewo jak na waykladzie
         """
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1
def f(v):
    if v.f>=0:
        return v.f
    x = v.fun
    for vi in v.emp:
        x+=g(vi)
    y = g(v)
    v.f = max(x,y)
    return v.f

def g(v):
    if (v.g >=0):
        return v.g
    v.g = 0
    for vi in v.emp:
        v.g+=f(vi)
    return v.g

t = TreeForTask(20)
t.build([6,10,5])

print(f(t.root))