a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

if a != b:
  a = max(a, b)
  b = max(a, b)
else:
  a = 0
  b = 0

print(f"a = {a}")
print(f"b = {b}")
