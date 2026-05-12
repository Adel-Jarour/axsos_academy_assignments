class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return
        return self.items[0]

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Output: 1
    print(q.peek())     # Output: 2
    print(q.size())     # Output: 2