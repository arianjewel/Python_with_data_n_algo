def left(i):
    return 2 * i

def right(i):
    return 2 * i + 1

def parent(i):
    return i // 2

def is_max_heap(H):
    n = len(H) - 1

    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False

        return True

def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)

    if l <= heap_size and heap[l] > heap [i]:
        largest = l
    else:
        largest = i

    if r <= heap_size and heap[r] > heap[largest]:
        largest = r

    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)

def build_max_heap(heap):
    heap_size = len(heap) - 1

    for i in range(heap_size // 2, 0, -1):
        max_heapify(heap, heap_size, i)

def heap_sort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1

    for i in range(heap_size, 1, -1):
        heap[1], heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)

def get_maximum(heap):
    return heap[1]

def extract_max(heap, heap_size):
    max_item = heap[1]
    heap[1] = heap[heap_size]
    heap_size -= 1
    max_heapify(heap, heap_size, 1)
    return max_item

def insert_node(heap, heap_size, node):
    heap_size += 1
    heap[heap_size] = node
    i = heap_size

    while i > 1 and heap[i] > heap[parent(i)]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)

    return heap_size

def increase_key(heap, i, new_value):
    heap[i] = new_value

    while i > 1 and heap[i] > heap[parent(i)]:
        heap[parent(i)], heap[i] = heap[i], heap[parent(i)]
        i = parent(i)


if __name__ == '__main__':
    heap = [None, 12, 7, 1, 3,10, 17, 19, 2, 5]
    print("before buiding heap", heap)
    heap_sort(heap)
    print("after buiding heap", heap)
