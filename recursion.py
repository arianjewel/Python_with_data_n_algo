
'''
def factorial(n):
    if n < 0:
        return None
    if n in [0, 1]:
        return 1

    return n * factorial(n-1)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(-1) == None
    assert factorial(5) == 120
'''







'''
def fibonacci(n):
    if n in [1, 2]:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)

def test_fibonacci():
    fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    for n, f in enumerate(fib):
        assert fibonacci(n+1) == f
'''








'''
def fibonacci(n):
    print("Trying to find fibonacci for", n)
    if n in [1, 2]:
        return 1

    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    print("5th fibonacci number is", fibonacci(5))
'''







'''
def print_number(n):
    print("try", n)
    if n == 0:
        return

    print_number(n-1)
    print(n)
print_number(5)
'''






def binary_search_recusive(L, left, right, x):
    if left > right:
        return -1

    mid = (left+right)//2

    if L[mid] == x:
        return mid

    if L[mid] > x:
        return binary_search_recusive(L, left, mid-1, x)

    else:
        return binary_search_recusive(L, mid+1, right, x)


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    left = 0
    right = len(L)-1

    for x in range(1,11):
        position = binary_search_recusive(L, left, right, x)

        if position == -1:
            if x in L:
                print(x, "is in L, but function returned -1")
            else:
                print(x, "not in list")

        else:
            if L[position] == x:
                print(x, "found in correct position")
            else:
                print("binary_search_recusive returned", position, "for", x, "which is not correct")

    print("program terminated!")
