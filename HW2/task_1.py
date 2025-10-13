number = input("Введите слово из латинских букв:\n")

if len(number) % 2 == 0:
    print(number[int(len(number) / 2) - 1:int(len(number)/2) + 1])
else:
    print(number[int(len(number) / 2)])