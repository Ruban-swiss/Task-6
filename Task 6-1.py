given_list = [10, 501, 22, 37, 100, 999, 87,  351]

# List of even numbers
even_list = [num for num in given_list if num % 2 == 0]

# List of odd numbers
odd_list = [num for num in given_list if num % 2 != 0]

# Print the lists
print("Even list:", even_list)
print("Odd list:", odd_list)