from collections import *


def bfs(n, m, edges, s):
    Q = deque()
    distance = [float("inf")] * (n+1)
    visited = [False] * (n+1)
    visited[s] = True
    distance[s] = 0
    graph = [[] for _ in range(n+1)]

    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])
    Q.append(s)
    while len(Q) > 0:
        u = Q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                distance[v]= distance[u]+6
                Q.append(v)

    i = 0
    distance.pop(0)
    distance.pop(s-1)
    while (i<len(distance)):
        if (distance[i]==float("inf")):
            distance[i]=-1
        i+=1
    return distance


bfs(5, 3 ,[[1, 2], [1, 3], [3, 4]], 1)
