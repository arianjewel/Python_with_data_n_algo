"""
def selection_sort(L):
    i = 0
    n = len(L)
    while i < n-1:
        index_min = i
        j = i+1
        while j < n:
            if L[j] < L[index_min]:
                index_min = j
            j+=1
        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]
        i+=1
"""
def selection_sort(L):
    n = len(L)
    for i in range(0, n-1):
        index_min = i
        for j in range(i+1, n):
            if L[j] < L[index_min]:        # IN THIS LINE '>' SIGN WILL SORT BIG TO SMALL
                index_min = j
        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]

if __name__=="__main__":
    L=[9,2,1,2,0,7]
    print("Before Sort:", L)
    selection_sort(L)
    print('After sort:', L)
