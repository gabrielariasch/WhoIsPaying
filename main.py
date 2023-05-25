import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(",")

length = len(names)
print(length)

random = random.randint(0, length -1)
print(random)


print(f"{names[random]} is paying the bill")