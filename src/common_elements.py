def common_elements(list1, list2):
    common = []  # Initialize an empty list to store common elements
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2
    
    # Iterate over both lists until one of them is exhausted
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            # If elements are equal, add to common list
            # Check if the common list is empty or if the last element added is different to avoid duplicates
            if not common or common[-1] != list1[i]:
                common.append(list1[i])
            i += 1  # Move pointer for list1
            j += 1  # Move pointer for list2
        elif list1[i] < list2[j]:
            i += 1  # Move pointer for list1 if current element is smaller
        else:
            j += 1  # Move pointer for list2 if current element is smaller
    
    # Print the list of common elements
    print("Common elements:", common)

# Test cases
common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])  # Output: [4, 5]
common_elements([1, 2, 3], [4, 5, 6])  # Output: []
common_elements([1, 2, 3, 4, 5], [1, 3, 5])  # Output: [1, 3, 5]
