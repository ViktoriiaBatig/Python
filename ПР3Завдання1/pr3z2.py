x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())


distance_A = (x1**2 + y1**2) ** 0.5
distance_B = (x2**2 + y2**2) ** 0.5


if distance_A < distance_B:
   print("Точка A ближче до початку координат.")
elif distance_B < distance_A:
   print("Точка B ближче до початку координат.")
else:
   print("Точки рівновіддалені від початку координат.")


