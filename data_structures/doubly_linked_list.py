from typing import Any, Optional


class DoublyNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional['DoublyNode'] = None
        self.prev: Optional['DoublyNode'] = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self.length = 0

    def append(self, data: Any) -> None:
        new_node = DoublyNode(data)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node   # type: ignore
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data: Any) -> None:
        new_node = DoublyNode(data)
        self.length += 1
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def remove(self, ind: int) -> None:
        if not self.head:
            raise IndexError("Cannot remove from empty list")

        if ind == 0:
            self.head = self.head.next
            self.head.next.prev = self.head     # type: ignore
            self.length -= 1
            return

        if ind == self.length - 1:
            self.tail = self.tail.prev      # type: ignore
            self.tail.next = None       # type: ignore
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
        prev_node.next.prev = prev_node     # type: ignore
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
