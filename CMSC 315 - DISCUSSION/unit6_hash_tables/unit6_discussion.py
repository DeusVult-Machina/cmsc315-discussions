"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # 1. Creating an empty dictionary to act as our hash table
    # Python dictionaries are implemented as hash tables under the hood.
    # When we add a key, Python computes a hash value for that key to determine
    # exactly where in memory the associated value should be stored.
    server_registry = {}

    # 2. Adding 5 key-value pairs (Simulating a network server registry)
    server_registry["192.168.1.1"] = "Router"
    server_registry["192.168.1.10"] = "Database_Primary"
    server_registry["192.168.1.11"] = "Database_Replica"
    server_registry["192.168.1.20"] = "Web_Server_01"
    server_registry["192.168.1.50"] = "Mail_Server"

    # 4. Displaying the contents
    print("Current Server Registry:", server_registry)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # 3. Explaining lookups: Because dictionaries use hashing, looking up a value
    # by its key is generally an O(1) operation. Python hashes the key we provide,
    # jumps directly to that memory address, and retrieves the value.

    # 1 & 2. Retrieving two existing keys and displaying results
    primary_db = server_registry["192.168.1.10"]
    web_server = server_registry.get("192.168.1.20")

    print(f"Lookup for '192.168.1.10': {primary_db}")
    print(f"Lookup for '192.168.1.20': {web_server}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print(f"Before update: {server_registry['192.168.1.20']}")

    # 1. Updating an existing key
    server_registry["192.168.1.20"] = "Web_Server_01_MAINTENANCE"

    # 3. Explaining updates: When we assign a new value to an existing key,
    # Python calculates the hash for the key, finds the existing entry in the
    # hash table, and overwrites the old value with the new one.

    # 2. Displaying after update
    print(f"After update: {server_registry['192.168.1.20']}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Registry before deletion:", list(server_registry.keys()))

    # 1. Deleting a key-value pair
    del server_registry["192.168.1.11"]

    # 3. Explaining deletions: Using 'del' or '.pop()' hashes the key, locates
    # the bucket in the hash table, and removes the reference to the key-value pair,
    # freeing up that space (or marking it as deleted to preserve probing chains).

    # 2. Displaying after deletion
    print("Registry after deletion:", list(server_registry.keys()))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Safely looking up a missing key
    # If we use bracket notation (server_registry["10.0.0.1"]), the program will crash
    # with a KeyError. Using the .get() method returns None (or a specified default) safely.
    missing_lookup = server_registry.get("10.0.0.1", "Not Found")
    print(f"Edge Case 1 (Missing Key Lookup): Attempted to find '10.0.0.1', result was '{missing_lookup}'")

    # Edge Case 2: Safely deleting a missing key
    # Attempting to 'del' a non-existent key throws a KeyError. We can use .pop() with a
    # default argument to safely attempt a deletion without crashing.
    deleted_item = server_registry.pop("10.0.0.99", "Key did not exist")
    print(f"Edge Case 2 (Missing Key Deletion): Attempted to delete '10.0.0.99', result was '{deleted_item}'")


if __name__ == "__main__":
    main()