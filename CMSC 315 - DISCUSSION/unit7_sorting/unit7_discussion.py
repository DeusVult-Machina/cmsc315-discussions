"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a copy of the original list to avoid modifying the input directly
    sorted_lst = lst.copy()
    n = len(sorted_lst)

    # Outer loop dictates how many passes we make through the list
    for i in range(n):
        # Track if any swaps happened in this pass to optimize early exits
        swapped = False

        # Inner loop compares adjacent elements (ignoring already sorted elements at the end)
        for j in range(0, n - i - 1):
            # If the current element is greater than the next, they are out of order
            if sorted_lst[j] > sorted_lst[j + 1]:
                # Swap the elements
                sorted_lst[j], sorted_lst[j + 1] = sorted_lst[j + 1], sorted_lst[j]
                swapped = True

        # If no swaps occurred in a full pass, the list is completely sorted
        if not swapped:
            break

    return sorted_lst


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Base case: A list of 0 or 1 elements is already sorted
    if len(lst) <= 1:
        return lst

    # Divide the list into two smaller halves
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Recursively sort both the left and right halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves back together and return the result
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list

    # Compare elements from both lists, appending the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Once one list is exhausted, append any remaining elements from the left list (if any)
    while i < len(left):
        result.append(left[i])
        i += 1

    # Append any remaining elements from the right list (if any)
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    print("\n=== DATASET #1 ===")
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    # Real-world scenario: Daily high temperatures for a week
    temperatures = [88, 72, 95, 64, 81, 77, 90]
    print(f"Original list (Temperatures): {temperatures}")
    print(f"Bubble Sort result:           {bubble_sort(temperatures)}")
    print(f"Merge Sort result:            {merge_sort(temperatures)}")


    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    print("\n=== DATASET #2 ===")
    print("TODO: Create a second dataset and compare sorting results.")

    # Real-world scenario: Product prices in a shopping cart
    cart_prices = [12.99, 4.50, 19.99, 0.99, 4.50, 45.00, 8.25, 2.50]
    print(f"Original list (Prices):       {cart_prices}")
    print(f"Bubble Sort result:           {bubble_sort(cart_prices)}")
    print(f"Merge Sort result:            {merge_sort(cart_prices)}")
    print("Comparison: Both algorithms produce the exact same sorted output, successfully handling decimals and duplicate values (4.50).")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Empty List
    empty_list = []
    print("\nEdge Case 1: Empty List")
    print(f"Original: {empty_list}")
    print(f"Bubble Sort: {bubble_sort(empty_list)}")
    print(f"Merge Sort: {merge_sort(empty_list)}")
    ## Explanation: Bubble sort immediately bypasses its inner loops because the length is 0. Merge sort triggers its base case (`len(lst) <= 1`) and returns the empty list immediately without crashing.

    # Edge Case 2: Already Sorted List
    sorted_list = [10, 20, 30, 40, 50]
    print("\nEdge Case 2: Already Sorted List")
    print(f"Original: {sorted_list}")
    print(f"Bubble Sort: {bubble_sort(sorted_list)}")
    print(f"Merge Sort: {merge_sort(sorted_list)}")
    ## Explanation: Because of the 'swapped' boolean flag I implemented, Bubble Sort only makes a single pass (O(N) time) and terminates early. Merge Sort, however, blindly splits and merges the list anyway, taking O(N log N) time despite the list already being sorted.


if __name__ == "__main__":
    main()