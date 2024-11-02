# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter=','):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))
    commmon_participants = sorted(participants1.intersection(participants2))  # Находим общих участников и сортируем их
    return commmon_participants


participants_first_group = "Иванов|Петров|Сидоров"  # Пример использования
participants_second_group = "Петров|Сидоров|Смирнов"
common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", common_participants)
