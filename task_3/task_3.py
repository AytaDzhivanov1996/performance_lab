import json

def fill_values(test, values_dict):
    # Заполняем значение для текущего теста
    if test["id"] in values_dict:
        test["value"] = values_dict[test["id"]]
    
    # Если у теста есть вложенные элементы, обрабатываем их рекурсивно
    if "values" in test:
        for child in test["values"]:
            fill_values(child, values_dict)

def main(values_path, tests_path, report_path):
    # Загрузка данных из JSON файлов
    with open(values_path, 'r') as f:
        values_data = json.load(f)["values"]

    with open(tests_path, 'r') as f:
        tests_data = json.load(f)["tests"]
    
    # Преобразование списка значений в словарь для удобства поиска
    values_dict = {item["id"]: item["value"] for item in values_data}
    
    # Заполнение значений
    for test in tests_data:
        fill_values(test, values_dict)
    
    # Запись результата в report.json
    with open(report_path, 'w') as f:
        json.dump({"tests": tests_data}, f, indent=4)

if __name__ == "__main__":
    # Пути к файлам
    values_path = "values.json"
    tests_path = "tests.json"
    report_path = "report.json"
    
    # Запуск основной функции
    main(values_path, tests_path, report_path)
