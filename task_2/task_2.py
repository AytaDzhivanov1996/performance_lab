import math

# Открываем файлы с данными
with open('circle.txt', 'r') as file_1, open('dot.txt', 'r') as file_2:
    # Читаем данные о центре и радиусе окружности
    cx, cy = map(float, file_1.readline().split())
    radius = float(file_1.readline())

    # Обрабатываем координаты точек
    for line in file_2:
        x, y = map(float, line.split())
        distance = math.sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius:
            print(1)
        elif distance == radius:
            print(0)
        else:
            print(2)
