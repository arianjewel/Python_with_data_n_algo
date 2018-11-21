'''
class Queue():
    """docstring for Queue."""
    def __init__(self):
        self.li = []

    def enqueue(self, item):
        return self.li.append(item)

    def dequeue(self):
         return self.li.pop(0)

    def is_empty(self):
        if not self.li:
            return True
        return False

if __name__ == '__main__':
    q=Queue()
    q.enqueue("Jewel")
    q.enqueue("Didar")
    q.enqueue("Mehedi")
    while not q.is_empty():
        person = q.dequeue()
        print(person)
'''




class Queue():
    """docstring for Queue."""
    def __init__(self, size):
        self.li = [0] * size
        self.max_size=size
        self.head, self.tail, self.size = 0, 0, 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")

            return

        print("Interesting!", item)
        self.li[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size+=1

    def dequeue(self):
        item = self.li[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return item

    def is_empty(self):
        if self.size == 0:
            return True

        return False

    def is_full(self):
        if self.max_size == self.size:

            return True

        return False

if __name__ == '__main__':
    q=Queue(3)
    q.enqueue("Jewel")
    q.enqueue("Didar")
    q.enqueue("Mehedi")
    q.enqueue("Takbir")

    while not q.is_empty():
        person = q.dequeue()
        print(person)

    q.enqueue("Subeen")
    q.enqueue("Masum")
    print(q.li)
    print("Head:", q.head)
    print("Tail:", q.tail)
