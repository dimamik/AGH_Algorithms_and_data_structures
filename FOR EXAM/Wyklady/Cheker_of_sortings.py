from random import *
import time
def Timer(func):
    def wrapper(*args,**kwargs):
        tic = time.perf_counter()
        output=func(*args,**kwargs)
        toc = time.perf_counter()
        print(toc)
        return output
    return wrapper
@Timer
def Checker(SortingFunc,k=150):
    positive=0
    all=k
    for i in range(k):
        tab=[]
        s=randint(10,999)
        for i in range(s):
            tab.append(randint(0,999))
        return_from_funct=SortingFunc(tab)
        if return_from_funct==sorted(tab):
            print("Test passed")
            positive+=1
        else:
            """ print(return_from_funct,sorted(tab)) """
            print("Test Failed")
    print("ALL TESTS PASSED WITH A SCORE", positive,"/",all)



Checker(sorted,1000)