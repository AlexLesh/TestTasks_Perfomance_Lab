import sys

def distance(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def point_position(center_x, center_y, radius, point_x, point_y):
    dist = distance(center_x, center_y, point_x, point_y)
    if dist == radius:
        return 0  # Точка лежит на окружности
    elif dist < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

def main():
    if len(sys.argv) != 3:
        print("Usage: python Task2.py file1 file2")
        return

    # Считываем координаты и радиус окружности
    circle_filename = sys.argv[1]
    with open(circle_filename, 'r') as circle_file:
        center_x, center_y = map(float, circle_file.readline().split())
        radius = float(circle_file.readline())

    # Считываем координаты точек и определяем их положение
    point_filename = sys.argv[2]
    with open(point_filename, 'r') as point_file:
        num_points = int(point_file.readline())
        for _ in range(num_points):
            point_x, point_y = map(float, point_file.readline().split())
            position = point_position(center_x, center_y, radius, point_x, point_y)
            print(position)

if __name__ == "__main__":
    main()