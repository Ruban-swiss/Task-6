given_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Count and store prime numbers in a list
prime_count = 0
prime_list = []

for num in given_list:
    if is_prime(num):
        prime_count += 1
        prime_list.append(num)

# Print the count and the list of prime numbers
print("Count of prime numbers:", prime_count)
print("List of prime numbers:", prime_list)