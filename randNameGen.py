import random

names = ["emma", "liam", "olivia", "noah", "ava", "elijah", "sophia", "james", "isabella", "william"]

# Get the number of names to generate from the user
num = int(input("Pick a number and see what random names come up? "))

# Use a for loop to print that many random names
for i in range(num):
    print(f"Name {i+1}: {random.choice(names)}")
