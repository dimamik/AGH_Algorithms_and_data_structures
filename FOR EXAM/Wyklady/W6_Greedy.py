def ActivitySelector(tab):
    i=0
    out=[]
    while i<len(tab):
        if i==0:
            prev=-1
        if prev<=tab[i][0]:
            prev=tab[i][1]
            out.append(tab[i])
        i+=1
    print(out)

ActivitySelector([[1,4],[3,5],[0,6],[5,7],[3,9],[5,9],[6,10],[8,11],[8,12],[2,14],[12,16]])
    
        
