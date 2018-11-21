'''
def selection_sort(L):
    n=len(L)
    i=1
    while i<n:
        item = i
        k=i-1
        for j in range(k,-1,-1):
            if L[j]>L[j+1]:
                break
            L[j+1]=L[j]
            L[j]=item
        i+=1
'''





def selection_sort(L):
    n = len(L)

    for i in range(1,n):
        item = L[i]
        j=i-1
        while j >= 0 and L[j] > item:
            L[j+1] = L[j]
            L[j] = item
            j-=1
        print(L)



if __name__ == '__main__':
    L=[6, 1, 4, 9, 2]
    print('Before Sort:', L)
    selection_sort(L)
    print('After Sort:', L)
