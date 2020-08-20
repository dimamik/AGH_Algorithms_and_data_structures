class Node:
    def __init__(self, key = None, taken = False):
        self.key = key
        self.taken = taken
        
    def __str__(self):
        if not self.taken:
            print('pusty')
        else:
            print('klucz: ', self.key)


def h(key):
    v = int('0b10101010', 2)
    for l in key:
        v ^= ord(l) % 255
    
    return v % N


N=11
hash_tab = [Node() for i in range(N)]


def recover(hash_tab):
    last_False_in_tab=-1
    for i in range(len(hash_tab)):
        if hash_tab[i].taken==False:
            last_False_in_tab=i
    last_False=-1
    Damaged_Element=-1
    Damaged_False=-1
    for i in range(len(hash_tab)):
        if hash_tab[i].key==None:
            continue
        if hash_tab[i].taken==False:
            last_False=i
        hash_index = h(hash_tab[i].key)
        if hash_index<i:
            if last_False>=hash_index:
                Damaged_Element=i
                Damaged_False = last_False
                hash_tab[Damaged_False].key=hash_tab[i].key
                hash_tab[Damaged_False].taken=True
                hash_tab[i].key=None
                hash_tab[i].taken=False
                if last_False_in_tab<i:
                    last_False_in_tab=i
                if last_False<i:
                    last_False=i
            pass
        elif hash_index>i:
            #Mamy dwie możliwości
            if last_False_in_tab>=hash_index or (last_False<i and last_False!=-1):
                Damaged_Element=i
                Damaged_False = last_False
                hash_tab[Damaged_False].key=hash_tab[i].key
                hash_tab[Damaged_False].taken=True
                hash_tab[i].key=None
                hash_tab[i].taken=False
                if last_False_in_tab<i:
                    last_False_in_tab=i
                if last_False<i:
                    last_False=i
            pass
    """ if Damaged_Element!=-1:
        hash_tab[Damaged_False].taken=True 
    """
    print(Damaged_Element) 




