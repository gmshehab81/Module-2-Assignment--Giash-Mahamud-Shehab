#Problem 2: Simple File Writing

name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

print("Your name has been saved to name.txt")
