import random

# random() - returns random float between 0.0 and 1.0(excluded)
print(random.random())
# randint(a,b) => returns random int between a and b ( both included)
print(random.randint(10,18))

nums = [68, 7, 84, 78, 232, 65]

# choice(sequence) => returns a random item from the sequence
print(random.choice(nums))

# shuffle(sequence) => returns the elements in random order
random.shuffle(nums)
print(nums)