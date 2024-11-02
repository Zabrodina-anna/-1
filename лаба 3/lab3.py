# TODO  Напишите функцию count_letters
def count_letters(text):
    lletter_counts = {}
    for char in text:
        if char.isalpha():
            lletter = char.lower()  # Приводим к нижнему регистру
            if lletter in lletter_counts:
                lletter_counts[lletter] += 1
            else:
                lletter_counts[lletter] = 1
    return lletter_counts


# TODO Напишите функцию calculate_frequency
def calculate_frequency(lletter_counts):
    total_letters = sum(lletter_counts.values())
    lletter_frequencies = {}
    for lletter, count in lletter_counts.items():
        friquency = count / total_letters
        lletter_frequencies[lletter] = round(friquency, 2)  # Округлим до двух знаков после запятой
    return lletter_frequencies


# основной текст
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
# Подсчет букв
letter_counts = count_letters(main_str)

# Вычисление частоты букв
letter_frequencies = calculate_frequency(letter_counts)

# Печать результатов
for letter, frequency in letter_frequencies.items():
    print(f"{letter}: {frequency:.2f}")
