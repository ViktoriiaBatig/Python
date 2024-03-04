# 1. Присвоєння числових значень змінним
num1 = 20
num2 = -8


# 2. Складні логічні вирази з оператором and
expr1 = (num1 > 0) and (num2 < 0)
expr2 = (num1 < 0) and (num2 > 0)
expr3 = (num1 > 0) and (num2 > 0)
expr4 = (num1 < 0) and (num2 < 0)


# 3. Складні логічні вирази з оператором or
expr5 = (num1 > 0) or (num2 < 0)
expr6 = (num1 < 0) or (num2 > 0)
expr7 = (num1 > 0) or (num2 > 0)
expr8 = (num1 < 0) or (num2 < 0)


# 4. Робота з рядковими змінними в логічних виразах
str1 = "Hello"
str2 = "World"
expr9 = (len(str1) > 0) and (len(str2) > 0)
expr10 = (len(str1) == 0) or (len(str2) == 0)


# 5. Виведення повідомлення в залежності від значення змінної
if num1 > 0:
   print("Значення змінної більше 0")
else:
   print("Значення змінної менше або дорівнює 0")


# 6. Вдосконалення попереднього коду
if num1 > 0:
   print(1)
else:
   print(-1)


# 7. Програма з описаними умовами
var1 = 11
var2 = 7
var3 = 0


if var1 > var2:
   var3 = var1 - var2
elif var1 < var2:
   var3 = var1 + var2
else:
   var3 = var1


# Виведення значення третьої змінної на екран
print("Значення третьої змінної:", var3)
