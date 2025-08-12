class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# TODO: реализовать удаление
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = DoublyNode(data)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        new_node = DoublyNode(data)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove(self, ind):
        if not self.head:
            raise IndexError("Cannot remove from empty list")

        if ind == 0:
            self.head = self.head.next
            self.head.next.prev = self.head
            self.length -= 1
            return

        if ind == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return

        prev_node = self.head
        for _ in range(ind - 1):
            if not prev_node.next:
                raise IndexError("Index out of range")
            prev_node = prev_node.next

        if not prev_node.next:
            raise IndexError("Index out of range")

        prev_node.next = prev_node.next.next
        prev_node.next.prev = prev_node
        self.length -= 1


linked_list = DoublyLinkedList()
linked_list.append("1st node - head")
linked_list.append("2nd node")
linked_list.append("3rd node - last")
linked_list.display()
linked_list.prepend("New head")
linked_list.display()
linked_list.remove(1)
linked_list.display()
