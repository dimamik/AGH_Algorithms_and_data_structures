""" !!WARNING!! """

def partition(arr, l, h): 
	i = ( l - 1 ) 
	x = arr[h] 

	for j in range(l, h): 
		if arr[j] <= x: 
			# increment index of smaller element 
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i] 
	arr[i + 1], arr[h] = arr[h], arr[i + 1] 
	return (i + 1) 
def q_sort(tab,l=0,r=-1):
    stack = [0] * (r-l+1)
    top = -1
    top+=1
    stack[top]=l
    top+=1
    stack[top]=r
    while top>=0:
        tmp_r=stack[top]
        top-=1
        tmp_l=stack[top]
        top-=1
        pivot = partition(tab,tmp_l,tmp_r)
        if pivot-1>tmp_l:
            top+=1
            stack[top]=tmp_l
            top+=1
            stack[top]=pivot-1
        if pivot+1<tmp_r:
            top+=1
            stack[top]=pivot+1
            top+=1
            stack[top]=tmp_r

tab=[4,1,2,5,4,1,2]
q_sort(tab,0,len(tab)-1)
print(tab)
