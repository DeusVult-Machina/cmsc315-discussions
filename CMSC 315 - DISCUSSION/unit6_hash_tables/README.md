# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

**1. What concepts or skills did you learn while completing this assignment?**
By completing this assignment, I reinforced my understanding of standard dictionary operations—inserting, looking up, updating, and deleting key-value pairs. I also learned how these high-level Python operations map directly to underlying hash table mechanics, where keys are processed by a hash function to compute a specific memory index.

**2. What challenges did you encounter, and how did you overcome them?**
The main challenge was handling missing keys during lookups and deletions without crashing the program with a `KeyError`. I overcame this by practicing edge-case handling. Instead of using strict bracket notation `[]`, I utilized `.get()` for safe lookups and `.pop(key, default)` for safe deletions, which gracefully fall back to default values when a key is absent.

**3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.**
Hash tables behave by taking an input (the key), passing it through a mathematical hash function, and using the resulting hash integer to store and locate the associated value in an array. A collision occurs when two distinct keys generate the exact same hash index. Python resolves this under the hood using a technique called open addressing, finding the next available slot. Because the hash function tells the program exactly where to look, hash tables drastically improve efficiency, allowing for near constant time ($O(1)$) lookups, insertions, and deletions regardless of how large the dataset grows.