class Queue:
    def __init__(self):
        self.items = []
        self.head = 0

    def enqueue(self, item):
        """Добавление элемента в конец очереди - O(1)"""
        self.items.append(item)

    def dequeue(self):
        """Удаление элемента из начала очереди - O(1)"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        item = self.items[self.head]
        self.head += 1

        if self.head > 100 and self.head > len(self.items) // 2:
            self.items = self.items[self.head:]
            self.head = 0
        return item

    def is_empty(self):
        """Проверка на пустоту"""
        return len(self.items) - self.head == 0

    def size(self):
        """Текущий размер очереди"""
        return len(self.items) - self.head

    def peek(self):
        """Посмотреть первый элемент без удаления"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[self.head]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.peek())
print(q.size())
