def Rotation(f,s):
    """ 
    Returns true jesli zgodnie z ruchiem zegarka, else false
     """
    x1,y1 = f
    x2,y2 = s 
    """ if ((x1*y1) - (x2*y1) == 0):
        if (y1 == y2):
            return x1<x2
        else:
            return False """
    return (x1*y1) - (x2*y1) < 0

# print(Rotation([1,2],[3,1]))
def PoleWielokata(tab_of_points):
    """ 
    Takes tab = [[1,2],[3,1],[4,3],[3,3]] which represents sorted points 
     """
    sum = 0
    prev = tab_of_points[0]
    for i in range(1,len(tab_of_points)+1):
        if (i == len(tab_of_points)):
            current = tab_of_points[0]
        else:
            current = tab_of_points[i]
        if (Rotation(prev,current)):
            pole = abs(prev[0] - current[0]) * max(prev[1], current[1])
            pole -= int (1/2 * (abs(prev[0] - current[0])) * abs((prev[1] -current[1])) )
            sum -= pole
            prev = current
        else:
            pole = abs(prev[0] - current[0]) * max(prev[1], current[1])
            pole -= int (1/2 * (abs(prev[0] - current[0])) * abs((prev[1] - current[1])) )
            sum += pole
            prev = current
            pass
    return sum
print(PoleWielokata([[1,2],[3,1],[4,3],[3,3]]))