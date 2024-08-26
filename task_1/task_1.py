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
    data = input("Введите числа n и m: ").split(' ')
    print(find_path(int(data[0]), int(data[1])))
