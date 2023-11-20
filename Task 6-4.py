
def sum_first_last_digit(n):
    # Convert the integer to a string to access the first and last digits easily
    num_str = str(n)
    first_digit = int(num_str[0])
    last_digit = int(num_str[-1])
    return first_digit + last_digit

# Test the function with a sample integer
sample_integer = 12345
result = sum_first_last_digit(sample_integer)
print(f"The sum of the first and last digits of {sample_integer} is {result}.")


