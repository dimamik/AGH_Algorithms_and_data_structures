""" not working """
class point():
    def __init__(self,value,is_end):
        self.is_end = is_end
        self.value = value
    def __lt__(self,value):
        return self.value < value.value
    def __str__(self):
        return str(self.value)
def zad(tab):
    tab_of_vertecies = []
    for i in range(len(tab)):
        tab_of_vertecies.append(point(tab[i][0],False))
        tab_of_vertecies.append(point(tab[i][1],True))
    tab_of_vertecies.sort()
    e = True
    for i in range(len(tab_of_vertecies)):
        if (tab_of_vertecies[i].is_end == False):
            
            if (e):
                print("J",end = "")
                e = False
            else:
                print("C",end = "")
                e = True
            
            
    #print(list(map(print,tab_of_vertecies)))
    
(zad([ (99, 150), (1, 100), (100, 301), (2,5), (150, 250)]))
