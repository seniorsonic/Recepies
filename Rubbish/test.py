def find_first_zero_index(numbers):
    for i, num in enumerate(numbers):
        if num == 0:
            return i
    return -1


user_input = input("Введите числа через пробел: ")
numbers = list(map(int, user_input.split()))
index = find_first_zero_index(numbers)
if index != -1:
    print(f"Индекс первого нулевого элемента: {index}")
else:
    print("В списке нет нулевых элементов.")
