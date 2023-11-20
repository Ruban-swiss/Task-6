given_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to find the sum of squares of digits of a number
def digit_square_sum(n):
    result = 0
    while n:
        result += (n % 10) ** 2
        n //= 10
    return result

# Function to check if a number is a happy number
def is_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = digit_square_sum(num)
    return num == 1

# Count the happy numbers
happy_count = sum(1 for num in given_list if is_happy_number(num))

# Print the count of happy numbers
print("Count of happy numbers:", happy_count)