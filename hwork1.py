#императивный стиль
def sort_list_imperative(numbers):
    for _ in range(0, len(numbers)-1):
        for i in range(0, len(numbers)-1):
            if numbers[i] < numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

# декларативный стиль
def sort_list_declarative(numbers):
    sort_numbers = sorted(numbers, reverse=True)
    return sort_numbers

def main():
    numbers = [5, 3, 7, -4, 1, 21]
    print(f"Исходный список: {numbers}")

    print(f"Cортировка в императивном стиле: {sort_list_imperative(numbers)}")
    print(f"Cортировка в декларативном стиле: {sort_list_declarative(numbers)}")

main()