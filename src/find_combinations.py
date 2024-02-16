def find_combinations(nums, target):
    # Define a nested function for backtracking
    def backtrack(start, target, path):
        # If the target is reached, add the current path to the result
        if target == 0:
            result.append(path)
            return
        # If target becomes negative, terminate the current branch
        if target < 0:
            return
        # Explore all possible combinations starting from 'start'
        for i in range(start, len(nums)):
            # Skip duplicates to avoid duplicate combinations
            if i > start and nums[i] == nums[i - 1]:
                continue
            # Recursively explore further combinations
            backtrack(i + 1, target - nums[i], path + [nums[i]])

    # Sort the input list to easily skip duplicates
    nums.sort()
    # Initialize an empty list to store the result
    result = []
    # Start backtracking from index 0 with the target sum and an empty path
    backtrack(0, target, [])
    return result

# Example usage with initialization in the main code
if __name__ == "__main__":
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    # Find combinations and print the result
    print(find_combinations(nums, target))
