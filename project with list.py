numbers = []
even_count = 0
odd_count = 0
n = int(input("How many numbers would you like?: "))

for i in range(n):
    num = int(input(f"Enter a number #{i+1}: "))
    numbers.append(num)

# Перевіряємо кожне число на парність
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

numbers.sort()
print("All numbers:\n ", numbers)
print("Sum:\n", sum(numbers))
print("Max:\n", max(numbers))
print("Average:\n", sum(numbers)/len(numbers))
print("Min:\n", min(numbers))
print("Sorted:\n", numbers)
print("Even numbers:\n", even_count)
print("Odd numbers:\n", odd_count)