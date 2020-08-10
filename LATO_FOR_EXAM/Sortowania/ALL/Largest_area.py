#
# Complete the 'getMaxArea' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER w
#  2. INTEGER h
#  3. BOOLEAN_ARRAY isVertical
#  4. INTEGER_ARRAY distance
#

def getMaxArea(w, h, isVertical, distance):
    first_area = w *h
    max_v = 0
    to_ret =[]
    array_of_witdh = [0] * (w+1)
    array_of_witdh[w]=1
    array_of_height = [0] * (h+1)
    for i in range(len(isVertical)):
        if (isVertical[i]==1):
            array_of_witdh[distance[i]]=1
        else:
            array_of_height[distance[i]] = 1

        #Chooose one in width and max in height
        
        i = 0
        is_second_time = False
        while (i < len(array_of_witdh)):
            tmp_width = 0
            if (is_second_time):
                tmp_width+=1
            tmp_height = 0
            while (i<len(array_of_witdh) and array_of_witdh[i] == 0):
                tmp_width += 1
                i += 1
            tmp_i = i
            j = 0
            while (j+1 < len(array_of_height) and array_of_height[j] == 0):
                tmp_height += 1
                j+=1
            max_v = max(max_v,tmp_height*tmp_width)
            i = tmp_i+1
            is_second_time =True
        to_ret.append(max_v)
        max_v=0
    return to_ret
    # Write your code here


print(getMaxArea(4,4,[0,1],[3,5]))
