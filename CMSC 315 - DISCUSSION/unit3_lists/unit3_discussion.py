"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    lst.insert(index, value)
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    pass


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    if index < 0 or index >= len(lst):
        return None
    pass


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            # Return the index if the value is found.[cite: 1]
            return i

    # Return -1 if the value is not found.[cite: 1]
    return -1
    pass


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    my_list = [20, 30, 40]
    print(f"Original list: {my_list}")

    insert_at(my_list, 0, 10)
    print(f"After inserting at the beginning: {my_list}"

    insert_at(my_list, 2, 25)
    print(f"After inserting in the middle: {my_list}")

    insert_at(my_list, len(my_list), 50)
    print(f"After inserting at the end: {my_list}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    removed_first = delete_at(my_list, 0)
    print(f"Removed '{removed_first}' from the beginning. Updated list: {my_list}")

    # 1. Delete an item from the middle (Index 2).[cite: 1]
    removed_middle = delete_at(my_list, 2)
    # 3. Display the updated list after each deletion.[cite: 1]
    print(f"Removed '{removed_middle}' from the middle. Updated list: {my_list}")

    # 1. Delete an item from the end (Last index).[cite: 1]
    removed_last = delete_at(my_list, len(my_list) - 1)
    print(f"Removed '{removed_last}' from the end. Updated list: {my_list}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    # 25 is expected to be at 1 in the index.
    found_idx = search_value(my_list, 25)
    print(f"Searching for 25 (exists). Result index: {found_idx}")

    # Search for a value that doesn't exist
    missing_idx = search_value(my_list, 999)
    print(f"Searching for 999 (does not exist). Result index: {missing_idx}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    # Edge Case 1: Delete using an invalid index.
    # Pass an index of 100 which exceeds the list bounds to test the validation.
    invalid_delete = delete_at(my_list, 100)
    print(f"Attempting to delete at invalid index 100. Returned: {invalid_delete}")

    # We create an empty list and immediately attempt to delete index 0.
    empty_list = []
    empty_delete = delete_at(empty_list, 0)
    print(f"Attempting to delete from an empty list. Returned: {empty_delete}")

if __name__ == "__main__":
    main()