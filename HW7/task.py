import csv # библиотека для чтения csv-файла

output_to_file = [] # список для сохрание результов парсирования

with open('web_clients_correct.csv', 'r', encoding='utf-8') as file: # открытие csv-файла
    reader = csv.reader(file)
    next(reader) # пропуск заголовка

    for row in reader:
        # получение данных из строки
        name = row[0]
        device = row[1]
        browser = row[2]
        sex = row[3]
        age = row[4]
        check = row[5]
        place = row[6]

        # определение о каком поле писать
        sex_text = "женского" if sex == "female" else "мужского"
        sex_act = "совершила" if sex == "female" else "совершил"

        # определение типа браузера
        browser_type = "десктопного" if device == "desktop" or device == "laptop" else "мобильного"

        # определение местоположения
        region = "Не указан" if place == "-" else place

        # формирование строки
        result = (f"Пользователь {name} {sex_text} пола, {age} лет {sex_act} покупку на {check} у.е. c {browser_type} браузера. "
                  f"Регион из которого совершалась покупка: {region}")

        # очистка строки от двойных пробелов
        result = " ".join(result.split())

        # сохранеие результата в список
        output_to_file.append(result)

# Сохраняем в файл
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(output_to_file))