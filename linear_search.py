'''

def linear_search(l,x):   # l is a list and x is which we wanna find from l list.
    n=len(l)
    i=0
    while i<n:
        if l[i]==x:
            return i
        i+=1
    i=-1
    return i

'''





def linear_search(l,x):         # l is a list and x is which we wanna find from l list.
    for i in range(len(l)):
        if l[i]==x:
            return i
        i+=1
    i=-1
    return i



def test():
    assert linear_search([1,2,3,4,5],5)==4,'your excepted value is wrong'
