import math
def Stopien(i):
	if i==0:return 0
	if i%4==0:return int (math.log2(i))
	return (math.ceil(math.log2(i)))
for i in range(20):
	print(i,Stopien(i))
