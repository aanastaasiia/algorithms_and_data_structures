def binary_search(number, list_of_numbers):
    low = 0
    high = len(list_of_numbers) - 1
    while low <= high:
        middle = (high + low) // 2
        if list_of_numbers[middle] == number:
            return middle
        elif number < list_of_numbers[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return None


def recursive_binary_search(number, list_of_numbers, low=0, high=None):
    if high is None:
        high = len(list_of_numbers) - 1
    if low <= high:
        middle = (high + low) // 2
        if list_of_numbers[middle] == number:
            return middle
        elif number < list_of_numbers[middle]:
            return recursive_binary_search(number, list_of_numbers, low, middle - 1)
        else:
            return recursive_binary_search(number, list_of_numbers, middle + 1, high)
    return None


arr = [-7, -2, -1, 0, 1, 2, 3, 5]
print(f"Бинарный поиск. Индекс элемента со значением 3 в списке {arr}: ", binary_search(3, arr))
print(f"Рекурсивная реализация бинарного поиска. Индекс элемента со значением 3 в списке {arr}: ", recursive_binary_search(3, arr))
