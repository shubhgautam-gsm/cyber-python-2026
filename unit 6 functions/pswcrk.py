import itertools

# Define the character set
characters = "0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+[]{}|;:,.<>?/`~"

# Function to generate all possible combinations for a given length
def generate_combinations(length):
    return [''.join(p) for p in itertools.product(characters, repeat=length)]

# Function to check if a password is correct
def check_password(password, target_password):
    return password == target_password

# Target password to crack
target_password = "12345678"

# Range of password lengths to try
min_length = 8
max_length = 18

# Brute-force the password for lengths from min_length to max_length
for length in range(min_length, max_length + 1):
    print(f"Trying passwords of length {length}...")
    combinations = generate_combinations(length)
    for combination in combinations:
        if check_password(combination, target_password):
            print(f"Password found: {combination}")
            exit()
    print(f"No password found for length {length}.")

print("Password not found in the given character set and length range.")



