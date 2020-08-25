"""  https://www.hackerrank.com/challenges/jack-goes-to-rapture/problem """



def getCost(g_nodes, g_from, g_to, g_weight):
    repr = [[0]*(g_nodes+1) for _ in range((g_nodes+1)) ]
    for i in range(len(g_from)):
        repr[g_from[i]][g_to[i]] = g_weight[i]
        repr[g_to[i]][g_from[i]] = g_weight[i]
    parents = (BellmanaForda(repr, 1, g_nodes))
    if (not parents or parents[g_nodes]==0):
        return "NO PATH EXISTS"
    curr = g_nodes
    max_val = repr[parents[curr]][curr]
    while curr != 0:
        max_val = max(repr[parents[curr]][curr], max_val)
        curr = parents[curr]
    return max_val

g_nodes,k =  (input().rstrip().split())
g_nodes = int(g_nodes)
k = int(k)
g_from,g_to,g_weight = [],[],[]
for _ in range(k):
    uvw = list(map(int, input().rstrip().split()))
    g_from.append(uvw[0])
    g_to.append(uvw[1])
    g_weight.append(uvw[2])
print(getCost(g_nodes ,g_from, g_to ,g_weight))
