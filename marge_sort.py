def marge(a, b):
    marged_list = []
    len_a, len_b = len(a), len(b)
    index_a, index_b = 0, 0

    while index_a < len_a and index_b < len_b:
        if a[index_a] < b[index_b]:
            marged_list.append(a[index_a])
            index_a += 1

        else:
            marged_list.append(b[index_b])
            index_b += 1

    if index_a < len_a:
        marged_list.extend(a[index_a:])
    elif index_b < len_b:
        marged_list.extend(b[index_b:])

    return marged_list


def marge_sort(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2

    left = marge_sort(L[:mid])
    right = marge_sort(L[mid:])

    return marge(left, right)


if __name__ == '__main__':

    L = [[4, 7, 2, 3], [10], [10, 9, 8, 7, 6], [2, 3, 1], [1, 2], [2, 1]]

    for li in L:
        sorted_list = marge_sort(li)
        print("Original List:", li)
        print("sorted list:", sorted_list)
        print()




    '''
    scenarios = [
        {"a": [1], "b": [2], "excepted": [1, 2]},
        {"a": [2], "b": [1], "excepted": [1, 2]},
        {"a": [], "b": [1, 2], "excepted": [1, 2]},
        {"a": [1, 2], "b": [], "excepted": [1, 2]},
        {"a": [1, 3, 5, 6], "b": [2, 4, 7, 8], "excepted": [1, 2, 3, 4, 5, 6, 7, 8]},
        {"a": [1], "b": [2, 3, 4], "excepted": [1, 2, 3, 4]},
        {"a": [1, 3, 5, 6], "b": [2, 3, 5, 6], "excepted": [1, 2, 3, 3, 5, 5, 6, 6]},
    ]
    for item in scenarios:
        marged_list = marge(item["a"], item["b"])

        try:
            assert item["excepted"] == marged_list

        except AssertionError:
            print("Output didn't match excepted Output")
            print("excepted:", excepted_marge_list)
            print("got:", marged_list)
'''
