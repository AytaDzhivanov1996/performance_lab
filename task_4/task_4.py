def min_moves_to_equal_elements(nums):
    # Сортируем массив
    nums.sort()
    
    # Находим медиану
    median = nums[len(nums) // 2]
    
    # Считаем количество шагов, чтобы привести все элементы к медиане
    moves = sum(abs(num - median) for num in nums)
    
    return moves

if __name__ == "__main__":
    # Читаем файл и преобразуем его в список чисел
    with open('numbers.txt', 'r') as file:
        nums = list(map(int, file.readlines()))
    
    # Вычисляем минимальное количество шагов
    result = min_moves_to_equal_elements(nums)
    
    # Выводим результат
    print(result)
