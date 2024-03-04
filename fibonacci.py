# Функція для обчислення чисел Фібоначчі
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Виведення ряду Фібоначчі від 5 до 20
fib_series = fibonacci(20)[4:]
print(f"Ряд Фібоначчі від 5-го до 20-го члена: {fib_series}")
# Виведення ряду парних чисел від 0 до 20
even_numbers = list(range(0, 21, 2))
print(f"Парні числа від 0 до 20: {even_numbers}")

# Виведення кожного третього числа в ряді від -1 до -21
third_numbers = list(range(-1, -22, -3))
print(f"Кожне третє число від -1 до -21: {third_numbers}")
