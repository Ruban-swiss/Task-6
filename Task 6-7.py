
def first_non_repeating_element(nums):
    # Create a dictionary to store the frequency of each element
    frequency_dict = {}

    # Count the frequency of each element in the list
    for num in nums:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    # Iterate through the list to find the first non-repeating element
    for num in nums:
        if frequency_dict[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None

# for Example :
my_list = [2, 3, 4, 2, 4, 6, 7, 8, 3]
result = first_non_repeating_element(my_list)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found in the list.")

