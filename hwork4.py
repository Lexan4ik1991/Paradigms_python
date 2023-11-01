import math
#Написать скрипт для расчета корреляции Пирсона между
#двумя случайными величинами (двумя массивами). Можете
#использовать любую парадигму.

arr1 = [4, 5, 4, 2, 12]
arr2 = [3, 4, 10, 9, 10]
#Массивы разной длины
arr3 = [1, 2, 3, 4, 5]
arr4 = [2, 4, 6, 8]
def correlation(arr1, arr2):
    if len(arr1) != len(arr2):
        raise ValueError("Error!!Массивы X и Y должны иметь одинаковую длину")

    n = len(arr1)
    mean_X = sum(arr1) / n
    mean_Y = sum(arr2) / n

    numerator = sum(map(lambda x, y: (x - mean_X) * (y - mean_Y), arr1, arr2))
    denominator = math.sqrt(sum(map(lambda x: (x - mean_X)**2, arr1))) * math.sqrt(sum(map(lambda y: (y - mean_Y)**2, arr2)))

    if denominator == 0:
        raise ValueError("Error!!Знаменатель равен нулю, деление на ноль невозможно")

    return numerator / denominator



correlation = round(correlation(arr1, arr2), 2)
print(correlation)

#correlation = correlation(arr3, arr4)
#print(correlation)
