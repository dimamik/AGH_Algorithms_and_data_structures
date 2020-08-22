""" https://www.hackerearth.com/ru/practice/algorithms/graphs/minimum-spanning-tree/practice-problems/algorithm/panda-and-destruction/ """


class Task():
    def __init__(self):
        nm = input().rstrip().split()
        n = int(nm[0])
        m = int(nm[1])
        repr = [[] for _ in range(n)]
        for _ in range(m):
            uv = input().rstrip().split()
            u = int(uv[0]) - 1
            v = int(uv[1]) - 1
            repr[u].append(v)
            repr[v].append(u)
        print(self.zad(repr))

    def zad(self, repr):
        c = 0
        for i in range(len(repr)):
            repr[i] = [len(repr[i]),i, repr[i]]
        repr = sorted(repr, reverse = True)
        for i in range(len(repr)):
            incidence = repr[i][2]
            if (len(incidence)==0):
                break
            c+=1
            v = repr[i][1]
            
            for u in incidence:
                """ Need to delete v in repr[x][2] """
                for k in range(len(repr)):
                    if (repr[k][1] == u):
                        if v in repr[k][2]:
                            repr[k][2].remove(v)
                            repr[k][0]-=1
                            break
                repr = sorted(repr,reverse=True)
        return c


Task()
