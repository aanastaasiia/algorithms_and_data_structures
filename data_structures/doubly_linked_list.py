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

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        new_node = DoublyNode(data)
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


linked_list = DoublyLinkedList()
linked_list.append("1st node - head")
linked_list.append("2nd node")
linked_list.append("3rd node - last")
linked_list.display()
linked_list.prepend("New head")
linked_list.display()
