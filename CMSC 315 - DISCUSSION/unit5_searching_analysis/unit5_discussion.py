"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
    pass


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # If the target is greater than the midpoint, we can entirely
            # discard the left half of the search space by moving 'low'.
            low = mid + 1
        else:
            # If the target is smaller, we can discard the entire right half.
            high = mid - 1

    return -1
    pass


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")
    #Small dataset created
    small_dataset = [10, 20, 30, 40, 50]

    # 2 & 3. Test both algorithms for existing and non-existing values
    print(f"Linear search for 30 (Exists): Index {linear_search(small_dataset, 30)}")
    print(f"Binary search for 30 (Exists): Index {binary_search(small_dataset, 30)}")

    print(f"Linear search for 99 (Not Found): Index {linear_search(small_dataset, 99)}")
    print(f"Binary search for 99 (Not Found): Index {binary_search(small_dataset, 99)}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # 1. Create a large sorted dataset (10,000 items)
    large_dataset = list(range(1, 10001))

    # 2 & 3. Test algorithms and compare
    print(f"Linear search for 9999: Index {linear_search(large_dataset, 9999)}")
    print(f"Binary search for 9999: Index {binary_search(large_dataset, 9999)}")
    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Empty list
    empty_list = []
    print(f"Searching an empty list: {binary_search(empty_list, 5)}")
    # Explanation: Because the list length is 0, 'high' becomes -1. The while loop
    # condition (low <= high) evaluates to False immediately, safely returning -1.

    # Edge Case 2: Value at the very first position in a single-element list
    single_list = [7]
    print(f"Searching for 7 in a single-item list: {binary_search(single_list, 7)}")
    # Explanation: 'low' and 'high' are both initialized to 0. The midpoint is 0, which
    # matches the target instantly. The index 0 is returned on the very first iteration.


if __name__ == "__main__":
    main()