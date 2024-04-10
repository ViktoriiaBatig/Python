import matplotlib.pyplot as plt

# Згенеруємо простий набір даних для візуалізації температури протягом тижня
days = ["Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]
temperatures = [22, 24, 19, 23, 25, 27, 21]  # Температура в градусах Цельсія

plt.figure(figsize=(10, 6))
plt.plot(days, temperatures, marker='o', linestyle='-', color='b')
plt.title('Температура протягом тижня')
plt.xlabel('День тижня')
plt.ylabel('Температура, °C')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
