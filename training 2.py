even_count = 0
odd_count = 0
min_number = None
max_number = None

while True:
    number = int(input("Type a number: "))

    if number == 0:
        break

    # Парні / непарні
    if number % 2 == 0:
        print("Even number")
        even_count += 1
    else:
        print("Odd number")
        odd_count += 1

    # Мінімальне число
    if min_number is None or number < min_number:
        min_number = number

    # Максимальне число
    if max_number is None or number > max_number:
        max_number = number

# Вивід результатів після циклу
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Minimum number:", min_number)
print("Maximum number:", max_number)