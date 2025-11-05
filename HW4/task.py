documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

def search_owner(search):
    for document in documents:
        if document['number'] == search:
            print(f"Результат:\n{document['name']}")
def search_shelf(search):
    for shelf, documents in directories.items():
        if search in documents:
            print(f"Документ хранится на полке:{shelf}")

while True:
    command = input("Введите команду:\n")
    if command == "p":
        search_owner(input("Введите номер документа:\n"))
    elif command == "s":
        search_shelf(input("Введите номер документа:\n"))
    elif command == "q":
        break
    else:
        print("Неизвестная комманда")