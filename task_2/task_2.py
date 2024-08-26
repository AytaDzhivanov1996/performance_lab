import math
import sys

# Открываем файлы с данными
with open(sys.argv[1], 'r') as file1, open(sys.argv[2], 'r') as file2:
    # Читаем данные о центре и радиусе окружности
    cx, cy = map(float, file1.readline().split())
    radius = float(file1.readline())

    # Обрабатываем координаты точек
    for line in file2:
        x, y = map(float, line.split())
        distance = math.sqrt((x - cx)**2 + (y - cy)**2)
        if distance < radius:
            print(1)
        elif distance == radius:
            print(0)
        else:
            print(2)
