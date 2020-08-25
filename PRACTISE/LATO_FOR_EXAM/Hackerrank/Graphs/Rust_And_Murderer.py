""" https://www.hackerrank.com/challenges/rust-murderer/problem """

def rustMurderer(n, roads, s):
    ns = range(1, n + 1)
    main_roads = {i:set() for i in ns}
    for a, b in roads:
        main_roads[a].add(b)
        main_roads[b].add(a)
    dist = {s:0}
    d = {s:0}
    nodes_left = [i for i in ns if i != s]
    l = 0
    nodes = [s]
    while nodes_left:
        new_left = []
        new_d = {}
        for child in nodes_left:
            found_road = False
            for parent, distance in d.items():
                if child not in main_roads[parent]:
                    new_d[child] = distance + 1
                    found_road = True
                    break
            if not found_road:
                new_left.append(child)
            else:
                dist[child] = new_d[child]
        print(dist, new_d, new_left)
        d = new_d
        nodes_left = new_left
    return [dist[i] for i in ns if i != s]

print(rustMurderer(4 , [[1, 2], [2, 3], [1, 4]] , 1))
