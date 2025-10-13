boys = []
girls = []
"""
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
"""
while True:
    temp = input("Введите мужчину (или 0 чтобы закончить ввод):\n")
    if temp == '0':
        break
    boys.append(temp)

while True:
    temp = input("Введите женщину (или 0 чтобы закончить ввод):\n")
    if temp == '0':
        break
    girls.append(temp)

if len(girls) == len(boys):
    boys.sort()
    girls.sort()
    print("Идеальные пары:")
    for boy, girl in zip(boys, girls):
        print(boy + " и " + girl)
else:
    print("Внимание, кто-то может остаться без пары.")

