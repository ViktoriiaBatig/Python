a = int(input("Введіть a: "))
b = int(input("Введіть b: "))
c = int(input("Введіть c: "))

count = 0

if a < 0:
  count += 1
if b < 0:
  count += 1
if c < 0:
  count += 1

print(f"Кількість негативних чисел: {count}")
