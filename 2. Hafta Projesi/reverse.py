l = [[1, 2], [3, 4], [5, 6, 7]]
l.reverse()

def ters(liste):
    for i in liste:
        if type(i) == list:
            i.reverse()
            ters(i)
    return liste

print(ters(l))
