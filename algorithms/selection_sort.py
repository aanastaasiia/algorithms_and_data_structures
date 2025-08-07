from typing import List

unordered_list = [6, 1, 7, 2, 8, 4, 87, 0, 9]


def selection_sort(list_to_sort: List[int]):
    length = len(list_to_sort)

    for i in range(length - 1):
        min_ind = i
        for j in range(i + 1, length):
            if list_to_sort[j] < list_to_sort[min_ind]:
                min_ind = j
        list_to_sort[i], list_to_sort[min_ind] = list_to_sort[min_ind], list_to_sort[i]
    return list_to_sort


print(selection_sort(unordered_list))
