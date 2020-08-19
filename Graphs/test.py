def func():
    visited = [0] * 10
    def func2():
        nonlocal visited
        visited[2] = 1
    func2()
    pass

func()