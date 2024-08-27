for i in range(21):
    print(i)

user_input = int(input("Enter a number: "))

if user_input % 2 == 0:
    print("Number is even")
else:
    print("Number is not even")

for i in range(21):
    if i % 2 == 0:
        print(i)

total_sum = 0

for number in range(50, 101):
    total_sum += number

print("The sum of numbers from 50 to 100 is:", total_sum)