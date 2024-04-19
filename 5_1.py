import random
import math
import numpy as np
import matplotlib.pyplot as plt

class GrahamScan():
       
    def distance(self, p0, p1):
        return (p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2

    # 3. Переопределение координат точек в полярной системе
    def polar_angle(self, p0, p1=None):
        y_span = p0[1] - p1[1]
        x_span = p0[0] - p1[0]
        return math.atan2(y_span, x_span)

    # 5. Построение выпуклой оболочки
    def graham_scan(self, points2d):
        start = min(points2d, key=lambda p: (p[1], p[0]))
        sorted_points = sorted(points2d, key=lambda p: (self.polar_angle(p, start), self.distance(p, start)))
        
        if len(sorted_points) < 3:
            return sorted_points  # Нельзя построить выпуклую оболочку менее чем из трех точек

        convex_hull = [sorted_points[0], sorted_points[1]]  # Начинаем с первых двух точек

        for p in sorted_points[2:]:
            while len(convex_hull) >= 2:
                # Вычисляем векторное произведение
                # a = последняя точка в выпуклой оболочке
                # b = предпоследняя точка в выпуклой оболочке
                a = convex_hull[-1]
                b = convex_hull[-2]
                cross_product = (a[0] - b[0]) * (p[1] - b[1]) - (a[1] - b[1]) * (p[0] - b[0])

                if cross_product > 0:  # Левый поворот
                    break  # Выходим из цикла, т.к. нашли левый поворот
                else:
                    convex_hull.pop()  # Удаляем последнюю точку из выпуклой оболочки и проверяем следующую

            convex_hull.append(p)  # Добавляем новую точку в выпуклую оболочку

        return convex_hull



def visualize(points, convex_hull):
    
    # 6. Визуализация результата
    plt.figure()
    for p in points:
        plt.plot(p[0], p[1], 'bp', color = 'k')
    for i in range(len(convex_hull)):
        plt.plot([convex_hull[i][0], convex_hull[(i + 1) % len(convex_hull)][0]],
                [convex_hull[i][1], convex_hull[(i + 1) % len(convex_hull)][1]], 'r--', marker = 'bp')
        
    plt.title('Визуализация выпуклой оболочки')
    plt.show() 

if __name__ == "__main__":
    # 1. Генерация случайного набора точек
    N = 100  # Количество точек
    points = [(np.random.normal(10, 3), np.random.normal(10, 3)) for _ in range(N)]
    convex_hull = GrahamScan().graham_scan(points)
    
    visualize(points=points, convex_hull=convex_hull)