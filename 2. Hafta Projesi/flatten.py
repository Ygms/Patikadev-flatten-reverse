l= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
k=[]
        
def flatten(liste):
    for i in liste:
        if type(i)== list:
            flatten(i)
        else:
            k.append(i)
    return k
print(flatten(l))
