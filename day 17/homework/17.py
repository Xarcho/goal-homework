family_members=["Maia","davit","Tamar","Nino","Gela","Nikoloz"]
print("Family Members:")
print("1. " + family_members[0])
print("2. " + family_members[1])
print("3. " + family_members[2])
print("4. " + family_members[3])
print("5. " + family_members[4])
print("6. " + family_members[5])

numbers = list(range(1, 11))
print("First element:", numbers[0])
print("Last element:", numbers[-1])

numbers = list(range(10, 21))
for i in range(0, len(numbers), 2):
    numbers[i] = 1
print(numbers)

customer_info = [
    input("Enter your first name: "),
    input("Enter your last name: "),
    input("Enter your age: "),
    input("Enter your place of residence: "),
    input("Enter your email address: ")
]
print("Customer Information:", customer_info)

last_name = "Kharabadze"
for i in range(len(last_name)):
    print(last_name[i])