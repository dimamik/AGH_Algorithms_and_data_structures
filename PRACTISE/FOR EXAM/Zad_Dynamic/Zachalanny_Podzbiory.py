def Zawieranie(first,second):
    """ 
    First zawiera się w second
     """
    k=(first[0]>=second[0] and second[1]>=first[1])
    return k
def delete_przedzial(tab_of_p,i):
    tab_of_p[i][0]=-1
    tab_of_p[i][1]=-1
first_out=-1
def zad(tab_of_p):
    global first_out
    first_out=-1
    tab_of_p=sorted(tab_of_p)
    print(tab_of_p)
    i=0
    while i<len(tab_of_p):
        """ Tu przechodze przez takie same początki """
        
        while i+1<len(tab_of_p) and tab_of_p[i][0]==tab_of_p[i+1][0]:
            tab_of_p[i][0]=-1
            tab_of_p[i][1]=-1
            main_p=tab_of_p[i+1]
            i+=1
        main_p=tab_of_p[i]
        i+=1
        while i<len(tab_of_p) and Zawieranie(tab_of_p[i],main_p):
            delete_przedzial(tab_of_p,i)
            i+=1
        #if i<len(tab_of_p) and tab_of_p[i][0]<=main_p[1]:
        first_out=i
            
        if i==len(tab_of_p):
            break
        i=first_out
    #i=max_ind
    i=0
    while i<len(tab_of_p):
        if tab_of_p[i][0]==-1:
            tab_of_p.remove(tab_of_p[i])

        else:
            i+=1
    return tab_of_p
tab_of_p=[[0,5],[1,3],[0,3],[2,7],[6,14],[7,14],[1,6]]
print(zad(tab_of_p))
            
