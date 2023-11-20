def has_sublist_with_zero_sum(lst):
    cumulative_sum = 0
    sum_set = set()

    for num in lst:
        cumulative_sum += num

        # Check if the cumulative sum repeats
        if cumulative_sum in sum_set or cumulative_sum == 0:
            return True

        # Add the cumulative sum to the set
        sum_set.add(cumulative_sum)

    # If no repeating cumulative sum is found, return False
    return False

# for Example:
my_list = [4, 2, -3, 1, 6]
result = has_sublist_with_zero_sum(my_list)

if result:
    print("There is a sub-list with a sum equal to zero.")
else:
    print("There is no sub-list with a sum equal to zero.")
