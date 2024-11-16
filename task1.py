import json


def task() -> float:
    with open('input.json', 'r') as file:  # открывает файл в режиме чтения
        data = json.load(file)  # считывает содержимое файла и преобразует его в объекты

    total_sum = sum(item['score'] * item['weight'] for item in
                    data)  # вычисления суммы произведений "score" и "weight" для каждого словаря в данных

    return round(total_sum, 3)  # округляет итоговую сумму до трех знаков после запятой


print(task())
