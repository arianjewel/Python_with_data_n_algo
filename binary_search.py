def binary_search(L,x):
    left, right = 0, len(L)-1
    while left <= right:
        mid = (left+right)//2
        if L[mid] == x:
            return mid
        if L[mid] > x:
            right = mid-1
        else:
            left = mid+1
    return -1

'''
def test():
    assert binary_search([1,2,3,4,5,6,7,8,9],9) == 8,"Excepted value is wrong"
'''

if __name__=="__main__":
    L = [1,2,3,4,5,6,7,8,9]
    for x in range(1,11):
        position = binary_search(L,x)

        if position == -1:
            if x in L:
                print(x, "is in L, but func return -1")
            else:
                print(x, "not in L")

        else:
            if L[position] == x:
                print(x, "found in correct position")
            else:
                print("binary_search returned", position, "for", x, "which is incorrect")
    print("Program terminated")
