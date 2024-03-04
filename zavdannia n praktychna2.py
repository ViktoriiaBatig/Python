def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

# Приклад використання:
number = int(input("Введіть натуральне число: "))
print("Сума цифр числа:", sum_of_digits(number))
