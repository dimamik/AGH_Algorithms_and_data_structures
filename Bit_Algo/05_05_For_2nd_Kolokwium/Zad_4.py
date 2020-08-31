def task(first,second):
    dic = {

        "aa": "b",
        "ab": "b",
        "bc": "a",
        "ba": "c",
        "bb": "b",
        "bc": "a",
        "ca": "a",
        "cb": "c",
        "c": "c",
    }
    return dic["" + first + second]

print(task("a","a"))

def get_num(symbol):
    dic = {
        "a":0,
        "b":1,
        "c":2
    }
    return dic[symbol]
def zad(string,last):
    """ 
    Using the dp function: F[i][j][k] - defines wheather it is possible to get symbol k connecting symbols from i to j in the string
     """
    F = [[[[] for _ in range(len(string))] for _ in range(len(string))] for _ in range(len(string))]
    F[0][0][get_num(string[0])] = 1
    F[0][1][get_num(task(string[0],string[1]))] = 1
    for i in range(len(string)):
        for j in range(len(string)):
            for barier in range(i,j):
                
zad("bbbbac","a")
