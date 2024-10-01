file = open("day24/my_file.txt")
contents = file.read()
print(contents)
file.close()

with open("day24/my_file.txt") as file:
    contents = file.read()
    print(contents)