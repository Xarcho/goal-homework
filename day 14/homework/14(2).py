for x in range(3):
  print(x)

for x in range(6):
  print(x)

adj = ["red", "yellow", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in range(6):
  if x == 7: break
  print(x)
else:
  print("Finally finished!")

