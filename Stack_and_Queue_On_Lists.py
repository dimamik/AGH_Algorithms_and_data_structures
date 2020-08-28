class Node():
    def __init__(self,el):
        self.next = None
        self.prev = None
        self.el = el

class Collection():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        self.isEmpty = True
    def pop(self):
        pass
    def get(self):
        pass
    def append(self,el):
        pass
    def push(self, el):
        pass