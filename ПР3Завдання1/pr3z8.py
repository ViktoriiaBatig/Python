# Введення чисел з клавіатури
a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

# Підрахунок кількості додатних чисел
positive_count = 0

if a > 0:
    positive_count += 1

if b > 0:
    positive_count += 1

if c > 0:
    positive_count += 1

# Виведення результату
print("Кількість додатних чисел серед a, b, c:", positive_count)
