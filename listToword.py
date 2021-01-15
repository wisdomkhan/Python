def stick(li):  # joining all chars stored in list to make a string
    n = ""
    for m in li:
        n += m
    return n


x = [i for i in input('enter chars\t').split()]
print(stick(x))
