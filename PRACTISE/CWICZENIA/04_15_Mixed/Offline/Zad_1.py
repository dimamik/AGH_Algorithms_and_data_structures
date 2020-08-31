""" 
Dana jest szachownica o wymiarach n×n. Każde pole (i, j) ma koszt (liczbę ze zbioru{1, . . . ,5}) umieszczonyw tablicy A (na polu A[j][i]). W lewym górnym rogu szachownicy (na pozycji (0,0) stoi król, którego zadaniem jest przejąść do prawego dolnego rogu, przechodząc po polach o minimalnym sumarycznym koszcie (jeśli królstoi na polu (i,j) to ponosi kosztA[j][i]; tak więc każda trasa zawiera koszt A[0][0] i A[n−1][n−1]). Proszę zaimplementować funkcje kingspath(A), która oblicza koszt sciezki króla. Funkcja powinna byc mozliwiejak najszybsza (w szczególności oczekujemy złożonościO(n2)).Państwa kod powinien mieć następującą postać (będzie uruchamiany; proszę nie usuwać fragmentu te-stującego; sprawdzający może także dołożyć swoje testy)
"""

""" 
1. Idziemy DFSem z arr[0][0] do arr[n-1][n-1] i wchodzimy do tego wierzchołku jak suma.curr jest mniejsza od poprzednio zakumulowanej w tym wierzchołku sumy



"""






""" ROW=3 
COL=3


class cell:

    def __init__(self,x=0,y=0,distance=0):
        self.x
        self.y
        self.distance


def operator(a,b):

    if a.distance == b.distance:
		if a.x != b.x:
			return a.x < b.x
		else:
			return a.y < b.y
    return a.distance < b.distance


def isInsideGrid(i, j):
	return (i >= 0 and i < COL and j >= 0 and j < ROW)


def shortest(grid, row, col):
    dis = [ROW][COL]
    for i in range(ROW):
        for j in range(COL):
            dis[i][j]=float('inf')
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    st = set()
    st.add(cell(0, 0, 0)) 

    dis[0][0] = grid[0][0]

    while (len(st)!=0): 
        k=st.pop()
        st.remove(st.pop()) 

        for i in range(4):
            x = k.x + dx[i]
            y = k.y + dy[i]
            if not isInsideGrid(x,y):
				continue 
            if dis[x][y] > dis[k.x][k.y] + grid[x][y]:
				if dis[x][y] != float('inf'):
					st.remove(st.find(cell(x, y, dis[x][y]))) 

				dis[x][y] = dis[k.x][k.y] + grid[x][y] 
				st.add(cell(x, y, dis[x][y])) 

	return dis[row - 1][col - 1] 


print(shortest([[1,1,2],[5,1,3],[4,1,1]],ROW,COL))
 """