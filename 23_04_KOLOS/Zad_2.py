""" 
Dzmitry Mikialevich
 """
""" 
Pomysl polega na tym, ze trzeba znalezc element pod ideksem len(T)-q-1 i len(T)-p-1 w tablice posortowanej rosnaco(Korzystajac z QuickSelect lub z Median of Medians (QuickSelect jest zawsze O(n)))
A dalej znalez wartosci koncow z tego przedzialu iterujac po tablice znajdziemy wszystkie
elementy z tego przedzialu.
Dalej trzeba posortowac ten "przedzial" -> Skoro to wzrosty (W>=0), mozna skorzystac z counting sorta, ale nie wiemy nic ani o jednostkach ani o przedziale tych liczb, wiec w moim rozwiazaniu skorzystalem z QuickSorta

Calkowita zlozonosc mojego algorytmu -> O(nlogn) (lub O(n) jesli uzyc counting sorta)
 """



def Lomuto_part(tab,low,high):
    pivot = tab[high]
    curr_index=low-1
    for i in range(low,high):
        if tab[i]<=pivot:
            curr_index+=1
            tab[i],tab[curr_index]=tab[curr_index],tab[i]
    tab[curr_index+1],tab[high]=tab[high],tab[curr_index+1]
    return curr_index+1
def q_sort(tab,low,high):
    if low<high:
        pivot_index=Lomuto_part(tab,low,high)
        q_sort(tab,low,pivot_index-1)
        q_sort(tab,pivot_index+1,high)
def reverse_elements(tab):
    new_tab=[0]*len(tab)
    index=len(tab)-1
    for i in range(len(tab)):
        new_tab[index]=tab[i]
        index-=1
    return new_tab
def MedianOfMedians(tab, j):
    """ 
    Dziala w O(n) zawszde (Magiczne Piatki)
    Zamiast nich mozna uzywac QuickSelect (Jest zaimplementowany ponizej)
     """
    if len(tab) < 10:
        """ 
        Mozna posortowac w czasie stalym O(10) 
         """
        q_sort(tab,0,len(tab)-1)
        return tab[j]
    S = []
    tab_ind = 0
    while tab_ind+5 < len(tab)-1:
        S.append(tab[tab_ind:tab_ind+5])
        tab_ind += 5
    S.append(tab[tab_ind:])
    Meds = []
    for tab_tmp in S:
        Meds.append(MedianOfMedians(tab_tmp, int((len(tab_tmp)-1)/2)))
    med = MedianOfMedians(Meds, int((len(Meds)-1)/2))
    tab1 = []
    tab2 = []
    tab3 = []
    for i in tab:
        if i < med:
            tab1.append(i)
        elif i > med:
            tab3.append(i)
        else:
            tab2.append(i)
    if j < len(tab1):
        return MedianOfMedians(tab1, j)
    elif j < len(tab2) + len(tab1):
        return tab[0]
    else:
        return MedianOfMedians(tab3, j-len(tab1)-len(tab2))

""" 
QuickSelect (Mozna uzyc zamiast) Zamiast Median of Medians (jesli nie mozna uzywac median of medians)
    def QuickSelect(tab,k,l,r): 
        
        if (k > 0 and k <= r - l + 1): 
    
            index = Lomuto_part(tab, l, r) 

            if (index - l == k - 1): 
                return tab[index] 

            if (index - l > k - 1): 
                return QuickSelect(tab, l, index - 1, k)
            return QuickSelect(tab, index + 1, r,  
                                k - index + l - 1) 
        return float("inf") 

 """
def section(T,p,q):
   
    p_v=MedianOfMedians(T,len(T)-p-1)
    q_v=MedianOfMedians(T,len(T)-q-1)
    """ 
    Lub ewentualnie QuickSelect dla znajdowania p_v i q_v
     """
    print(p_v,q_v)
    tab_g=[]
    for i in range(len(T)):
        if T[i]<=p_v and T[i]>=q_v:
            tab_g.append(T[i])
    print(tab_g)
    q_sort(tab_g,0,len(tab_g)-1)
    tab_g=reverse_elements(tab_g)
    print (tab_g)




lister = [ 2,1,3,5]

section(lister,0,3)
