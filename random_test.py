import random

# Generate a random integer
random_int = random.randint(1, 100)
print(f"Random Integer: {random_int}")

# Generate a random float
random_float = random.uniform(1.0, 100.0)
print(f"Random Float: {random_float:.2f}")

# Select a random element from a list
choices = ["Bitcoin", "Ethereum", "Litecoin", "Ripple"]
random_choice = random.choice(choices)
print(f"Random Choice: {random_choice}")

# Shuffle a list
shuffle_list = [1, 2, 3, 4, 5]
random.shuffle(shuffle_list)
print(f"Shuffled List: {shuffle_list}")
