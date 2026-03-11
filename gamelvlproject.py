# Порожні списки
users = []
level = []

# Цикл для 2 гравців
for i in range(3):
    name = input(f"Введи ім'я гравця #{i+1}: ")
    lvl = int(input(f"Введи рівень гравця #{i+1}: "))
    users.append(name)
    level.append(lvl)

# Виводимо всіх гравців
print("\nСписок всіх гравців:")
for i in range(len(users)):
    print(f"{users[i]} — рівень {level[i]}")

# Знаходимо максимальний рівень
max_level = max(level)
max_index = level.index(max_level)  # індекс гравця з найвищим рівнем

# Виводимо гравця з найвищим рівнем
print(f"\nГравець з найвищим рівнем: {users[max_index]} — рівень {max_level}")
