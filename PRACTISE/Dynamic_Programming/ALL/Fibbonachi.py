def Fibb(n):
    last=1
    prev=1
    print(last,prev)
    for _ in range(n-2):
        print(last+prev)
        tmp=last+prev
        last=prev
        prev=tmp
Fibb(10)


