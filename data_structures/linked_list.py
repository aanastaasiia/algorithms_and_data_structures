from typing import Any


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode со значением {self.val}"


def add_to_end(head: ListNode, val: Any) -> None:
    ptr = head
    while ptr.next:
        ptr = ptr.next
    ptr.next = ListNode(val)


def add_to_front(head: ListNode, val: Any) -> ListNode:
    node = ListNode(val)
    node.next = head
    return node


# Создает и расширяет список
head = ListNode(5)
add_to_end(head, 'abc')
add_to_end(head, 4.815162342)

# Вывод
print(head)  # ListNode со значением 5
print(head.next)  # ListNode со значением abc
print(head.next.next)  # ListNode со значением 4.815162342

# Пытаемся обновить head
add_to_front(head, 0)
print(head)  # ListNode со значением 5
