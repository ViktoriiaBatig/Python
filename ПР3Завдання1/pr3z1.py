def process_numbers(a, b, c):
  """
  Підносить до квадрата невід'ємні числа та до четвертої
  ступеня - від'ємні.

  Args:
    a: Перше число.
    b: Друге число.
    c: Третє число.

  Returns:
    Кортеж з трьох чисел, де невід'ємні числа піднесені
    до квадрата, а від'ємні - до четвертої
    ступеня.
  """
  result = []
  for num in (a, b, c):
    if num >= 0:
      result.append(num ** 2)
    else:
      result.append(num ** 4)
  return tuple(result)

# Приклад використання
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

result = process_numbers(a, b, c)
print(f"Результат: {result}")
