enemies = 1

def increase_enemies():
    global enemies
    enemies = "two"
    print(f"inside function = {enemies}")


increase_enemies()

print(f"outside function {enemies}")
