import sys

def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))
    current_index = 0
    path = []

    while len(circular_array) > 0:
        next_index = (current_index + m - 1) % len(circular_array)
        path.append(circular_array.pop(next_index))
        current_index = next_index

    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python Task1.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    if n <= 0 or m <= 0:
        print("И как n, так и m должны быть положительными целыми числами.")
        sys.exit(1)

    path = circular_array_path(n, m)
    print("".join(map(str, path)))