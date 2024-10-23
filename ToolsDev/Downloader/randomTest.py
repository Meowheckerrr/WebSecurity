import random

def generate_unique_numbers(count, range_start=0, range_end=999999):

    return random.sample(range(range_start, range_end + 1), count)

# Generate unique random numbers
unique_numbers = generate_unique_numbers(1)
print(unique_numbers[0])
