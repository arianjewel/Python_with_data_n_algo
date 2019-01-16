def counting_sort(L, n):
    count = [0] * (n+1)
    for x in L:
        count[x] = count[x] + 1

    sorted_list = []

    for index, value in enumerate(count):
        if value > 0:
            sorted_list.extend([index] * value)

    return sorted_list

if __name__ == '__main__':
    L = [3, 4, 1, 6, 2, 4, 9, 7, 8, 4, 2, 1]
    sorted_list = counting_sort(L, 9)
    print(sorted_list)
