class Stack:
    """Реализация стека (LIFO) с использованием списка."""

    def __init__(self, items=None):
        """Инициализация стека. Можно передать начальные элементы."""
        self._items = list(items) if items else []

    def push(self, item):
        """Добавляет элемент на вершину стека."""
        self._items.append(item)

    def pop(self):
        """Удаляет и возвращает элемент с вершины стека."""
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Возвращает элемент с вершины стека без удаления."""
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def clear(self):
        """Очищает стек."""
        self._items.clear()

    def __len__(self):
        """Возвращает количество элементов в стеке."""
        return len(self._items)

    def __bool__(self):
        """Проверяет, есть ли элементы в стеке."""
        return bool(self._items)

    def __iter__(self):
        """Итерация по стеку (от вершины к основанию)."""
        return reversed(self._items)

    def __repr__(self):
        """Строковое представление стека."""
        return f"Stack({self._items})"

    def __contains__(self, item):
        """Проверка наличия элемента в стеке."""
        return item in self._items


s = Stack([1, 2, 3])
s.push(4)
print(s)
print(s.pop())
print(s.peek())
print(len(s))

for item in s:
    print(item)

