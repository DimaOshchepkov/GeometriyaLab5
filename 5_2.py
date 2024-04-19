import random
import numpy as np

import matplotlib.pyplot as plt

#Находим самую левую и самую нижнюю точку из списка.
def leftmost_point(points):
    return min(points, key=lambda p: (p[0], p[1]))

#Возвращает положительное значение, если p-q-r образуют левый поворот.
#Возвращает отрицательное, если правый поворот.
#Возвращает 0, если точки на одной линии.
def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

#Алгоритм Джарвиса для поиска выпуклой оболочки.
def jarvis_march(points):
    if len(points) < 3:
        return points

    convex_hull = []
    left_point = leftmost_point(points)
    p = left_point

    while True:
        convex_hull.append(p)
        q = points[0] if points[1] == p else points[1]
        for r in points:
            if (orientation(p, q, r) > 0):
                q = r
        p = q
        if p == left_point:
            break

    return convex_hull




def visualize(points, convex_hull):
    plt.figure(figsize=(8, 6))  # Задаем размеры графика (8 дюймов в ширину и 6 дюймов в высоту)
    
    # Визуализация точек
    for p in points:
        plt.plot(p[0], p[1], 'bp', color = 'k', markersize=8)  # Голубые точки
    
    # Визуализация границ выпуклой оболочки
    for i in range(len(convex_hull)):
        plt.plot([convex_hull[i][0], convex_hull[(i + 1) % len(convex_hull)][0]],
                 [convex_hull[i][1], convex_hull[(i + 1) % len(convex_hull)][1]], 'r--',  marker = 'o')  # Зеленые пунктирные линии
    
    # Настройка внешнего вида графика
    plt.title('Визуализация выпуклой оболочки', fontsize=14)  # Заголовок графика
    plt.xlabel('X', fontsize=12)  # Название оси X
    plt.ylabel('Y', fontsize=12)  # Название оси Y
    plt.grid(True)  # Включаем сетку
    
    plt.show()  # Отображаем график
    
if __name__ == "__main__":
    # Генерация набора точек
    N = 50  # Количество точек
    points = [(np.random.normal(10, 3), np.random.normal(10, 3)) for _ in range(N)]
    convex_hull = jarvis_march(points)
    
    visualize(points, convex_hull)

