class Vertex():
    def __init__(self,value1,value2):
        self.value1=value1
        self.value2=value2
    """ 
    Nadpisuje por?wnywanie
     """
    def __lt__(self, value):
        return (self.value2<value.value2)

v = Vertex(5,2)
u = Vertex(1,3)
print(v>u)