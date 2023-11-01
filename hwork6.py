from typing import List

arr = [1, 2, 7, 6, 11, 33, 45]
def binary_search(arr: List[int], number: int) -> int:

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1

    return -1



print(f"Исходный массив: {arr}")
number = int(input("Введите искомый элемент: "))
result = binary_search(arr, number)

if result == -1:
    print("Искомого элемента нет в массиве")
else:
    print(f"Искомый элемент: {number} найден по индексу: {result}")
