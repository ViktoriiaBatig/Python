# Введення чисел з клавіатури
a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))
k = float(input("Введіть число k: "))

# Визначення дільників
divisors = []

if a % k == 0:
    divisors.append("a")

if b % k == 0:
    divisors.append("b")

if c % k == 0:
    divisors.append("c")

# Виведення результату
if divisors:
    print(f"{k} є дільником чисел {', '.join(divisors)}")
else:
    print(f"{k} не є дільником жодного з чисел a, b, c.")
