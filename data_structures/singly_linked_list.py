from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional['Node'] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data: Any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
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
            return

        prev_node = self.head
        for _ in range(ind - 1):
            if not prev_node.next:
                raise IndexError("Index out of range")
            prev_node = prev_node.next

        if not prev_node.next:
            raise IndexError("Index out of range")

        prev_node.next = prev_node.next.next


linked_list = SinglyLinkedList()
linked_list.append("1st node - head")
linked_list.append("2nd node")
linked_list.append("3rd node - last")
linked_list.display()
linked_list.prepend("New head")
linked_list.display()
linked_list.remove(1)
linked_list.display()
