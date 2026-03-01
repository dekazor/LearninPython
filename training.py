total = 0

while True:
    number = int(input("Type a number: "))

    if number == 0:
        break

    total += number

print("Sum =", total)