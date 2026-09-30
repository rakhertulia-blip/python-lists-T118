def retest_scores(scores):
    result = []

    for score in scores:
        if score < 70:
            result.append(score)

    return sorted(result)


def replace_score(scores, number, value):
    if number < 1 or number > len(scores):
        return False

    if value < 0 or value > 100:
        return False

    scores[number - 1] = value
    return True


def corrected_copy(table, row_number, column_number, value):
    if row_number < 1 or row_number > len(table):
        return None

    if column_number < 1 or column_number > len(table[0]):
        return None

    if value < 0 or value > 100:
        return None

    result = []

    for row in table:
        result.append(row.copy())

    result[row_number - 1][column_number - 1] = value

    return result


# Задание 6
scores = [80, 40, 70, 55, 40]

print("Исходный список:", scores)
print("На повторную проверку:", retest_scores(scores))
print("После функции:", scores)


# Задание 7
scores = [80, 65, 90, 45, 70]

print("\nЗадание 7")
print("Исходные оценки:", scores)

while True:
    try:
        number = int(input("Введите номер оценки: "))
        value = int(input("Введите новую оценку: "))
    except ValueError:
        print("Ошибка! Введите целые числа.")
        continue

    if replace_score(scores, number, value):
        break

    print("Ошибка! Проверьте номер и оценку от 0 до 100.")

print("Изменённый список:", scores)

average = sum(scores) / len(scores)
print("Среднее:", average)

print("Повторная проверка:", retest_scores(scores))


# Задание 8
print("\nЗадание 8")

table = [
    [70, 80],
    [60, 90]
]

print("Исходная таблица:", table)

new_table = corrected_copy(table, 1, 2, 100)

print("Новая таблица:", new_table)
print("Исходная таблица:", table)

print("Неверная строка:", corrected_copy(table, 0, 2, 100))
print("Неверный столбец:", corrected_copy(table, 1, 3, 100))
print("Неверная оценка:", corrected_copy(table, 1, 2, -1))