import sys

def find_path(n, m):
    array = list(range(1, n+1))
    path = []
    current_index = 0

    while True:
        path.append(array[current_index])
        current_index = (current_index + m - 1) % len(array)
        if current_index == 0:
            break

    return ''.join(map(str, path))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 task_1.py <n> <m>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
        print(find_path(n, m))
    except ValueError:
        print("Invalid input. n and m must be integers.")
        sys.exit(1)
