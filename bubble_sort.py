'''
def bubble_sort(L):
    n=len(L)
    i=0
    while i < n-1:
        j=0
        while j < n-i-1:
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
            j+=1
        i+=1
        print(L)
'''






'''
def bubble_sort(L):
    n=len(L)
    exchange = True
    for i in range(0, n-1):
        exchange = False
        for j in range(0, n-i-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                exchange = True
        if exchange is False:
            break
        print(L)
'''






def bubble_sort(L):
    n=len(L)-1
    exchange  = True

    while n > 0 and exchange:
        exchange = False
        for i in range(n):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                exchange = True
        n-=1
        print(L)



        


if __name__ == '__main__':
    L=[9,2,1,2,7,0]
    print("Before Sort:", L)
    bubble_sort(L)
    print('After sort:', L)
