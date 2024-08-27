import json
import sys

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
    values_path = sys.argv[1]
    tests_path = sys.argv[2]
    report_path = sys.argv[3]
    
    if len(sys.argv) != 4:
        print("Usage: python3 task_3.py <path_to_values_file.json> <path_to_tests_file.json> <path_to_report_file.json>")
        sys.exit(1)

    # Запуск основной функции
    main(values_path, tests_path, report_path)
    print(f"Report in {report_path}")
