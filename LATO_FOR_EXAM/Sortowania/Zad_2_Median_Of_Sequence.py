""" 
https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem

!Counting sort need to be used!
 """
import tab
import statistics
def Median(arr):
    """ 
    Takes sorted array and returns its median
     """
    if (len(arr) % 2 == 0):
        
        return (arr[len(arr)//2 - 1] +arr[len(arr)//2] )/2
    else:
        return arr[len(arr)//2]

def Zad(arr,d,first_time_executed = true):
    tab_c =[0] * 201
    warning =0
    first = 0
    curr_tab_c = [None] * 201
    sorted_tab = []
    tab_to_return = [0]*(d)
    for i in range(len(arr)):
        if (i<d):
            tab_c[arr[i]]+=1
        else:
            tmp_i = i
            for j in range(len(tab_c)):
                curr_tab_c[j]=tab_c[j]
            if (first_time_executed):
                first_time_executed = false
                for i in range(1, len(tab_c)):
                    curr_tab_c[i] += curr_tab_c[i-1]
                for j in range(d-1, -1, -1):
                    index_in_ret = curr_tab_c[arr[j]]-1
                    tab_to_return[index_in_ret] = arr[j]
                    curr_tab_c[arr[j]] -= 1
            i = tmp_i
            median = Median(tab_to_return)
            k=arr[i]
            if k>= 2 * median:
                warning+=1
            tab_c[arr[i]]+=1
            tab_c[arr[first]]-=1
            first+=1
    return warning
    pass
print(Zad(tab.tab,20000))
