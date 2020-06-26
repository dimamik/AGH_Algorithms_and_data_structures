def Bucket_Sort(tab,n=False):
    """ 
    Dziala tylko dla jednostajnego rozkladu danych z przedziaÅ‚u
    [0,n]
     """
    """ 
    Rozdielnosc Bucketa -> parametr dla najlepszego rozkladu
    Im lepiej rozklad, tym mniej zlozonosc """
    """ 
    Rozd Bucketa ->       max_el/ilosc_elementow
    Ilosc Bucketow ->     Max_el/rozd_Bucketa=ilosc_elementow
    ind Bucketa dla el -> El/rozd_Bucketa
    !! USES APPEND !!
     """
    max_el=max(tab)
    if n==False:
        n=len(tab)
    
    rozd_Bucketa=max_el/len(tab)

    Buckets=[[] for _ in range(n+1)]
    for number in tab:
        index_of_Bucket=int (number/rozd_Bucketa)
        Buckets[index_of_Bucket].append(number)
        j=len(Buckets[index_of_Bucket])-2

        while j>=0 and Buckets[index_of_Bucket][j]<number:
            Buckets[index_of_Bucket][j+1]=Buckets[index_of_Bucket][j]
            j-=1
        Buckets[index_of_Bucket][j+1]=number
    for i in range(n+1):
        Buckets[i]=sorted(Buckets[i])
    to_return=[]
    for i in range(n+1):
        for j in range(len(Buckets[i])):
            to_return.append(Buckets[i][j])
    return to_return





