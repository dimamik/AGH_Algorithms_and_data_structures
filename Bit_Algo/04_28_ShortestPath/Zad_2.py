""" 
Dany jest grafważony G, oraz drzewo rozpinające T, które być może jest drzewem
najkrótszych ścieżek w G, od pewnego wierzchołka s z G. Podaj algorytm, który
sprawdzi, czy T rzeczywiście jest drzewem najkrótszych ścieżek od wierzchołka s. 
 """

""" 

Trzeba zrobić relaxację dla każdego wierzchołku, jak nie bedzie ani razu zrobiona, to wszystko git, else not git
O(V)

for e in E:
	if relax(e):
		return False
return True

relax(e):
	if d(s,v) + w(e) < d(s,u):
		return True
	return False

 """