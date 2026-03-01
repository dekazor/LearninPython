count = 0
total = 0
odd_number = 0
evn_number = 0
abs_number = None

while True:
    number = int(input("Type a number: "))
    if number == 0:
        break

    total += number
    count += 1

    if number % 2 == 0:
        evn_number += 1

    if number % 2 == 1:
        odd_number += 1

    if abs_number is None or abs(number) > abs_number:
        abs_number = abs(number)

    average = total / count

print("Even numbers:", evn_number)
print("Odd numbers:", odd_number)
print("Average number:", average)
print("Total number:", total)
print("Max number:", abs_number)

