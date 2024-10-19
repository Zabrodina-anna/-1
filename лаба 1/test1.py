numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
ob = len(numbers)  # Общее количество элементов, включая None
summa = sum(numbers for numbers in numbers if numbers is not None) # Cумма всех элементов, не включая None
arifm = summa / (ob)  # Вычисляем среднее арифметическое
# TODO заменить значение пропущенного элемента средним арифметическим
numbers[numbers.index(None)] = arifm # Заменяем None на среднее арифметическое
print("Измененный список:", numbers)
