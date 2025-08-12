from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    else:
        mid = arr[0]
        less = [i for i in arr if i < mid]
        equal = [i for i in arr if i == mid]
        more = [i for i in arr if i > mid]
        return quick_sort(less) + equal + quick_sort(more)


unsorted_list = [4, 6, 1, 0, -9, 5, 10, 66, 43]
print(quick_sort(unsorted_list))
