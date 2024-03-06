angle_a = float(input("Введіть величину першого кута: "))
angle_b = float(input("Введіть величину другого кута: "))

if angle_a + angle_b < 180:
  print("Трикутник існує.")
  if angle_a == 90 or angle_b == 90:
    print("Трикутник прямокутний.")
  else:
    print("Трикутник не прямокутний.")
else:
  print("Трикутник не існує.")
