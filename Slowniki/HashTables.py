
def add_to_hash(tab,val_to_add):
    tmp=val_to_add
    val_to_add=str (val_to_add)
    hash_ind=hash(val_to_add)%len(tab)
    print(hash_ind)
    if tab[hash_ind]==0:
        tab[hash_ind]=tmp
    else:
        first_ind=hash_ind
        i=1
        while tab[hash_ind]!=0:
            hash_ind=(hash_ind+i)%len(tab)
            i+=1
            if first_ind==hash_ind:
                return "Brak Wolnego Miejsca"
        tab[hash_ind]=tmp
    return tab

    

print(add_to_hash([0,1,2,0,4,9,45,0,1,0],4568))