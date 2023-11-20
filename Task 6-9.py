def find_triplet_with_sum(lst, target_sum):
    n = len(lst)

    # Iterate through each triplet combination
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                triplet_sum = lst[i] + lst[j] + lst[k]
                
                # Check if the triplet sum is equal to the target sum
                if triplet_sum == target_sum:
                    return (lst[i], lst[j], lst[k])

    # If no such triplet is found, return None
    return None

# for Example:
my_list = [10, 20, 30, 9]
target_sum = 59
result_triplet = find_triplet_with_sum(my_list, target_sum)

if result_triplet:
    print(f"Triplet with sum {target_sum}: {result_triplet}")
else:
    print(f"No triplet found with sum {target_sum}")
