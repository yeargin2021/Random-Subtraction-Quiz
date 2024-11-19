import random

while True:
    x = round((random.random() * 10), 2)
    b = round((random.random() * 10), 2)

    if x > b:
        x, b = b, x

    c = input(f"{b} - {x} = ")

    if c.lower() == "exit":  # Move exit condition above comparison and make it case-insensitive
        break

    try:
        user_input = float(c)
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_input != round((b - x), 2):
        print(f"Incorrect: the answer is {round((b - x), 2)}")
    else:
        print("Correct!")

print("Goodbye!")