"""
Парсинг дат из различных газетных форматов
"""

from datetime import datetime

# 1. The Moscow Times — Wednesday, October 2, 2002
moscow_times_str = "Wednesday, October 2, 2002"
moscow_times_format = "%A, %B %d, %Y"  # Полное название дня недели, полное название месяца, день, год
moscow_times_date = datetime.strptime(moscow_times_str, moscow_times_format)
print(f"The Moscow Times: {moscow_times_str}")
print(f"Формат: {moscow_times_format}")
print(f"Результат: {moscow_times_date}")
print(f"Проверка (обратный формат): {moscow_times_date.strftime(moscow_times_format)}\n")

# 2. The Guardian — Friday, 11.10.13
guardian_str = "Friday, 11.10.13"
guardian_format = "%A, %d.%m.%y"  # Полное название дня недели, день.месяц.год (двухзначный год)
guardian_date = datetime.strptime(guardian_str, guardian_format)
print(f"The Guardian: {guardian_str}")
print(f"Формат: {guardian_format}")
print(f"Результат: {guardian_date}")
print(f"Проверка (обратный формат): {guardian_date.strftime(guardian_format)}\n")

# 3. Daily News — Thursday, 18 August 1977
daily_news_str = "Thursday, 18 August 1977"
daily_news_format = "%A, %d %B %Y"  # Полное название дня недели, день, полное название месяца, год
daily_news_date = datetime.strptime(daily_news_str, daily_news_format)
print(f"Daily News: {daily_news_str}")
print(f"Формат: {daily_news_format}")
print(f"Результат: {daily_news_date}")
print(f"Проверка (обратный формат): {daily_news_date.strftime(daily_news_format)}\n")

# Сводная таблица форматов
print("=" * 60)
print("СВОДНАЯ ТАБЛИЦА ФОРМАТОВ ДАТ:")
print("=" * 60)
print(f"{'Газета':<20} {'Формат даты':<30} {'Формат для datetime.strptime()':<40}")
print("-" * 90)
print(f"{'The Moscow Times':<20} {'Wednesday, October 2, 2002':<30} {'%A, %B %d, %Y':<40}")
print(f"{'The Guardian':<20} {'Friday, 11.10.13':<30} {'%A, %d.%m.%y':<40}")
print(f"{'Daily News':<20} {'Thursday, 18 August 1977':<30} {'%A, %d %B %Y':<40}")
print("=" * 90)

# Проверка всех дат на корректность
print("\nПРОВЕРКА КОРРЕКТНОСТИ ПРЕОБРАЗОВАНИЙ:")
dates = [
    (moscow_times_str, moscow_times_format, moscow_times_date),
    (guardian_str, guardian_format, guardian_date),
    (daily_news_str, daily_news_format, daily_news_date)
]

for original_str, fmt, date_obj in dates:
    try:
        # Прямое преобразование
        parsed = datetime.strptime(original_str, fmt)
        # Обратное преобразование для проверки
        reconstructed = parsed.strftime(fmt)
        is_correct = (original_str == reconstructed)
        print(f"✓ {original_str:<30} -> {parsed.date()} (корректно: {is_correct})")
    except ValueError as e:
        print(f"✗ {original_str:<30} -> ОШИБКА: {e}")

# Пример использования с другими датами для проверки понимания форматов
print("\nПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ФОРМАТОВ С ДРУГИМИ ДАТАМИ:")
test_dates = [
    ("Monday, January 15, 2024", moscow_times_format),
    ("Sunday, 31.12.23", guardian_format),
    ("Tuesday, 25 December 2024", daily_news_format)
]

for date_str, fmt in test_dates:
    try:
        date_obj = datetime.strptime(date_str, fmt)
        print(f"  {date_str:<30} ({fmt}) -> {date_obj.date()}")
    except ValueError as e:
        print(f"  {date_str:<30} ({fmt}) -> ОШИБКА: {e}")
```