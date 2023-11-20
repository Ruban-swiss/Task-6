def distribute_mangoes(bags, students):
    # Step 1: Sort the list of bags
    sorted_bags = sorted(bags)

    # Step 2: Create M buckets
    buckets = [[] for _ in range(students)]

    # Step 3: Distribute bags in a round-robin fashion
    for i in range(len(sorted_bags)):
        buckets[i % students].append(sorted_bags[i])

    # Calculate the difference between the max and min mangoes in each bucket
    differences = [max(bucket) - min(bucket) for bucket in buckets]

    return differences

# for Example:
bags = [5, 4, 3,1]
students = 2
result = distribute_mangoes(bags, students)
print(result)
