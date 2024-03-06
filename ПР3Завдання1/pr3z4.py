x = float(input("Введіть x: "))
y = float(input("Введіть y: "))

if x < y:
  x = (x + y) / 2
  y = 2 * x * y
else:
  y = (x + y) / 2
  x = 2 * x * y

print(f"x = {x}")
print(f"y = {y}")

