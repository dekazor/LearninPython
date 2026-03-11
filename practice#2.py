name = input("enter your name: ")
total = 0
fruit =  ["apple", "banana", "cherry"]
fruit.append("orange")
fruit.pop(1)
grade = int(input("enter your grade: "))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

for i in range (0, grade + 1):
    total += i

print(f"Hello {name}")
print(fruit)
print(letter)
print(total)

