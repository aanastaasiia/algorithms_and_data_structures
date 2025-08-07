from typing import List


def bubble_sort(list_to_sort: List[int]) -> List[int]:
    length = len(list_to_sort)
    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = (
                    list_to_sort[j + 1],
                    list_to_sort[j],
                )
                swapped = True
        if not swapped:
            break
    return list_to_sort


arr = [5, 1, 6, 8, 9, 22]
print(bubble_sort(arr))
