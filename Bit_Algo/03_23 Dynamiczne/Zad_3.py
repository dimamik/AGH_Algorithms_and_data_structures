""" Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną wartość z jednego z 
końców tablicy i dodajemy do swojej sumy, a następnie to samo robi nasz przeciwnik. Zakładając, że 
przeciwnik gra optymalnie, jaką maksymalną sumę możemy uzbierać?  
“Uogólniony problem paczki mentosów” """


def mentos(arr,start,end):
    if start==end:
        return arr[start]
    if end-start==1:
        return max(arr[start],arr[end])
    sum_from_start_to_end=start
    #... Koniec na filmiku