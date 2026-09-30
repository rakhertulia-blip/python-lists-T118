# ЕКЕВ Т118: Практическая работа со списками (Задания 4-7)

def read_scores(count: int) -> list[int]:
    """Задание 4: Ввод count корректных целых оценок (от 0 до 100)."""
    scores = []
    while len(scores) < count:
        try:
            current_num = len(scores) + 1
            val = int(input(f"Введите оценку №{current_num} (от 0 до 100): "))
            if 0 <= val <= 100:
                scores.append(val)
            else:
                print("Ошибка: Допустимо от 0 до 100.")
        except ValueError:
            print("Ошибка: Введите целое число.")
    return scores


def show_statistics(scores: list[int]) -> None:
    """Задание 5: Вывод статистики по списку оценок."""
    if not scores:
        print("Нет результатов")
        return

    total_count = len(scores)
    total_sum = sum(scores)
    avg_score = round(total_sum / total_count, 2)
    min_score = min(scores)
    max_score = max(scores)

    passed_count = 0
    for score in scores:
        if score >= 70:
            passed_count += 1
    failed_count = total_count - passed_count

    print("\n--- Статистика качества ЕКЕВ ---")
    print(f"Количество: {total_count}")
    print(f"Сумма: {total_sum}")
    print(f"Среднее: {avg_score}")
    print(f"Минимум: {min_score}")
    print(f"Максимум: {max_score}")
    print(f"Прошли (>=70): {passed_count}")
    print(f"Остальные (<70): {failed_count}")


def retest_scores(scores: list[int]) -> list[int]:
    """Задание 6: Новый отсортированный список оценок ниже 70."""
    failed_scores = [score for score in scores if score < 70]
    return sorted(failed_scores)


def replace_score(scores: list[int], number: int, value: int) -> bool:
    """Задание 7: Изменение оценки по её номеру (начиная с 1)."""
    if 1 <= number <= len(scores) and 0 <= value <= 100:
        scores[number - 1] = value
        return True
    return False


def main():
    print("=== Задание 4: Ввод 5 оценок ===")
    scores = read_scores(5)
    print("\nСобраны оценки:", scores)

    print("\n=== Задание 5: Статистика ===")
    show_statistics(scores)

    print("\n=== Задание 6: Повторная проверка (<70) ===")
    retest = retest_scores(scores)
    print("Оценки на пересдачу:", retest)
    print("Исходный список не изменён:", scores)

    print("\n=== Задание 7: Исправление оценки по номеру ===")
    while True:
        try:
            num = int(input("\nВведите номер оценки для замены (от 1): "))
            new_val = int(input("Введите новую оценку (0-100): "))

            if replace_score(scores, num, new_val):
                print("Оценка успешно изменена!")
                break
            else:
                print("Ошибка: Некорректный номер или значение вне диапазона 0-100. Повторите ввод.")
        except ValueError:
            print("Ошибка: Вводимые данные должны быть целыми числами.")

    print("\n=== Итоговая статистика и список на пересдачу ===")
    show_statistics(scores)
    print("Обновленный список на повторную проверку:", retest_scores(scores))


if __name__ == "__main__":
    main()