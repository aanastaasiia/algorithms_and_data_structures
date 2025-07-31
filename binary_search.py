def binary_search(number, list_of_numbers):
    low = 0
    high = len(list_of_numbers) - 1
    while low <= high:
        middle = (high + low) // 2
        if list_of_numbers[middle] == number:
            return middle
        elif number<list_of_numbers[middle]:
            high = middle - 1
        else:
            low = middle + 1

print(binary_search(3, [-7, -2, -1, 0, 1, 2, 3, 5]))