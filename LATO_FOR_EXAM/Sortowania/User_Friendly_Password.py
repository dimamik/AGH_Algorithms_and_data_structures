""" ALL PASSED """

def ASCII(string):
    return ord(string)
def Hashing(string):
    p = 131
    M = 10**9 + 7
    hash_number = 0
    for i in range(len(string)):
        hash_number+=(ASCII(string[i]) * (p**(len(string)-i-1)))
    return hash_number%M
def Hashing_With_One_More_Char(string):
    p = 131
    M = 10**9 + 7
    hash_number = 0
    x = len(string) + 1
    for i in range(x-1):
        pot = (x-i-1)
        hash_number+=(ASCII(string[i]) * (p**pot))
    return hash_number%M

def authEvents(events):
    curr_password_int = 0
    curr_string_hashing = ""
    tab_ret = []
    for i in range(len(events)):
        if (events[i][0] == "setPassword"):
            #Set password
            curr_password_int = Hashing(events[i][1])
            curr_string_hashing = events[i][1]
            pass
        else:
            if (curr_password_int == int(events[i][1])):
                tab_ret.append(1)
            else:
                val =Hashing_With_One_More_Char(curr_string_hashing)
                val = int(events[i][1]) - val
                if (val >=0 and val <=127):
                    tab_ret.append(1)
                else:
                    tab_ret.append(0)
                pass
    return tab_ret


print(authEvents([["setPassword","Espinoza"],["authorize",Hashing("Espinoza")]]))