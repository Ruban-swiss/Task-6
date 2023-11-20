def find_duplicates(list1, list2, list3):
    # Combine the three lists into a single list
    combined_list = list1 + list2 + list3
    
    # Create a dictionary to store the frequency of each element
    frequency_dict = {}
    
    # List to store the duplicates
    duplicates = []
    
    # Iterate through the combined list
    for element in combined_list:
        # If the element is already in the dictionary, it's a duplicate
        if element in frequency_dict:
            # Add to the duplicates list if not already present
            if element not in duplicates:
                duplicates.append(element)
        else:
            # Add the element to the dictionary with a frequency of 1
            frequency_dict[element] = 1
    
    return duplicates

# Example lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [6, 7, 8, 9, 10]

# Find duplicates
duplicates = find_duplicates(list1, list2, list3)

# Print the result
if duplicates:
    print(f"The duplicates in the three lists are: {duplicates}")
else:
    print("There are no duplicates in the three lists.")
