def zad2(tab):
    tab=sorted(tab)
    tab_of_pairs=[None]*(len(tab)//2)
    j=len(tab)-1
    for i in range(len(tab)//2):
        tab_of_pairs[i]=(tab[i],tab[j])
        j-=1

    print(tab_of_pairs)

zad2([1,5,1000,1001])
